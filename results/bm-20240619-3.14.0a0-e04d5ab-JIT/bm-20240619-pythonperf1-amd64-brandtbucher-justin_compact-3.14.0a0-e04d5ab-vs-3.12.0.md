# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: windows-amd64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.07x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 82.9 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.31x faster                                                       |
| async_tree_none            | 291 ms                                                      | 225 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 598 ms: 1.29x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                                       |
| async_tree_io              | 731 ms                                                      | 599 ms: 1.22x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.0 ms: 1.38x faster                                                      |
| float          | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 82.4 ms: 1.06x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 18.5 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 167 us: 1.17x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.06x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.8 us: 1.03x faster                                                      |
| pickle               | 7.43 us                                                     | 7.27 us: 1.02x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.78 us: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.86 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (2): json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.19 ms: 1.36x faster                                                      |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.5 us: 1.53x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.45x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 46.7 ms: 1.43x faster                                                      |
| deepcopy                   | 238 us                                                      | 166 us: 1.43x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.51 sec: 1.39x faster                                                     |
| nbody                      | 71.9 ms                                                     | 52.0 ms: 1.38x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.37x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.19 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.31x faster                                                       |
| async_tree_none            | 291 ms                                                      | 225 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 598 ms: 1.29x faster                                                       |
| float                      | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.70 us: 1.23x faster                                                      |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 599 ms: 1.22x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.4 ms: 1.20x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 167 us: 1.17x faster                                                       |
| pyflate                    | 295 ms                                                      | 254 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.21 ms: 1.16x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.0 ms: 1.15x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.48 us: 1.15x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 751 us: 1.14x faster                                                       |
| logging_format             | 6.72 us                                                     | 5.91 us: 1.14x faster                                                      |
| raytrace                   | 192 ms                                                      | 170 ms: 1.13x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.2 ms: 1.13x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 12.7 ms: 1.13x faster                                                      |
| fannkuch                   | 247 ms                                                      | 219 ms: 1.12x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 462 ms: 1.11x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.8 ns: 1.10x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 956 ms: 1.09x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 57.6 ms: 1.09x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 82.9 ms: 1.08x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.1 ms: 1.07x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.65 us: 1.07x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.06x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 82.4 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                      |
| go                         | 91.6 ms                                                     | 87.4 ms: 1.05x faster                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 980 us: 1.04x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.8 us: 1.03x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 781 us: 1.03x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.8 ms: 1.03x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.27 us: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.13 ms: 1.02x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.1 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.13 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                     |
| unpickle_list              | 2.75 us                                                     | 2.78 us: 1.01x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 70.6 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.4 ms: 1.03x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                      |
| 2to3                       | 218 ms                                                      | 230 ms: 1.05x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 83.3 ms: 1.06x slower                                                      |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.86 us: 1.08x slower                                                      |
| richards_super             | 32.1 ms                                                     | 34.8 ms: 1.08x slower                                                      |
| richards                   | 28.4 ms                                                     | 31.0 ms: 1.09x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.57 ms: 1.11x slower                                                      |
| coverage                   | 40.8 ms                                                     | 45.6 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.13x slower                                                       |
| pycparser                  | 699 ms                                                      | 795 ms: 1.14x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 915 us: 1.22x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 72.3 ms: 1.23x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 18.5 ms: 1.30x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (4): asyncio_tcp, json_dumps, pickle_list, json
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (5) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown