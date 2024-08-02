# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: windows-amd64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 83.3 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 380 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 597 ms: 1.29x faster                                                       |
| async_tree_none            | 291 ms                                                      | 227 ms: 1.28x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| async_tree_io              | 731 ms                                                      | 604 ms: 1.21x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.6 ms: 1.42x faster                                                      |
| float          | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 82.2 ms: 1.06x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 17.3 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 168 us: 1.16x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.4 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 59.7 ms: 1.09x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 123 us: 1.08x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.05x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.86 us: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.70 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (3): pickle_list, json_dumps, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.24 ms: 1.35x faster                                                      |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.6 us: 1.52x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 45.1 ms: 1.48x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.44x faster                                                     |
| nbody                      | 71.9 ms                                                     | 50.6 ms: 1.42x faster                                                      |
| deepcopy                   | 238 us                                                      | 168 us: 1.42x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.1 us: 1.40x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.24 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 380 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 597 ms: 1.29x faster                                                       |
| async_tree_none            | 291 ms                                                      | 227 ms: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.72 us: 1.22x faster                                                      |
| async_tree_io              | 731 ms                                                      | 604 ms: 1.21x faster                                                       |
| scimark_fft                | 184 ms                                                      | 154 ms: 1.20x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.4 ms: 1.17x faster                                                      |
| pyflate                    | 295 ms                                                      | 253 ms: 1.16x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 168 us: 1.16x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.21 ms: 1.15x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.15x faster                                                      |
| raytrace                   | 192 ms                                                      | 169 ms: 1.14x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.53 us: 1.13x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.3 ms: 1.13x faster                                                      |
| logging_format             | 6.72 us                                                     | 5.94 us: 1.13x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 760 us: 1.13x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 932 ms: 1.12x faster                                                       |
| fannkuch                   | 247 ms                                                      | 220 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 460 ms: 1.11x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.4 ms: 1.11x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.7 ns: 1.11x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 12.9 ms: 1.10x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 57.2 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.7 ms: 1.09x faster                                                      |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 123 us: 1.08x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 83.3 ms: 1.08x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.3 ms: 1.07x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 82.2 ms: 1.06x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                      |
| go                         | 91.6 ms                                                     | 86.7 ms: 1.06x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.07 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.3 ms: 1.03x faster                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 991 us: 1.03x faster                                                       |
| sqlglot_parse              | 804 us                                                      | 781 us: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.1 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.12 ms: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.0 ms: 1.01x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 70.6 ms: 1.02x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                     |
| unpickle_list              | 2.75 us                                                     | 2.86 us: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 228 ms: 1.04x slower                                                       |
| async_generators           | 239 ms                                                      | 250 ms: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 83.0 ms: 1.05x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.9 ms: 1.06x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.7 ms: 1.06x slower                                                      |
| pycparser                  | 699 ms                                                      | 739 ms: 1.06x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.0 ms: 1.06x slower                                                      |
| sympy_expand               | 284 ms                                                      | 301 ms: 1.06x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.70 us: 1.06x slower                                                      |
| coverage                   | 40.8 ms                                                     | 44.4 ms: 1.09x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.49 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 67.7 ms: 1.15x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 903 us: 1.20x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.3 ms: 1.22x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (4): asyncio_tcp, pickle_list, json_dumps, pickle
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (5) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown