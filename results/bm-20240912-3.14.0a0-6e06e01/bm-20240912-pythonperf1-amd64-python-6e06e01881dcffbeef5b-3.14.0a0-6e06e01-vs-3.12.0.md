# Results vs. 3.12.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-amd64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.00x faster
- HPT reliability: 87.05%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 84.4 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.30x faster                                                       |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| float          | 56.8 ms                                                     | 56.1 ms: 1.01x faster                                                      |
| nbody          | 71.9 ms                                                     | 83.7 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 91.8 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.23 us: 1.03x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.5 us: 1.00x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.00 us: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.08x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.14x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                     |
| unpickle             | 8.18 us                                                     | 9.62 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.7 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.89 ms: 1.03x faster                                                      |
| django_template | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.38 sec: 1.52x faster                                                     |
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.30x faster                                                       |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.26x faster                                                       |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.4 us: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.08x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.64 us: 1.07x faster                                                      |
| go                         | 91.6 ms                                                     | 85.8 ms: 1.07x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.6 ms: 1.06x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 808 us: 1.06x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 84.4 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.5 ms: 1.05x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.8 ms: 1.03x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.89 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.23 us: 1.03x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 67.6 ms: 1.02x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.0 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.01x faster                                                      |
| float                      | 56.8 ms                                                     | 56.1 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.4 ms: 1.01x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 66.4 ms: 1.01x faster                                                      |
| chaos                      | 43.3 ms                                                     | 43.1 ms: 1.01x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 18.5 us: 1.00x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 63.1 ms: 1.00x slower                                                      |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| raytrace                   | 192 ms                                                      | 195 ms: 1.01x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| logging_simple             | 6.28 us                                                     | 6.43 us: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 62.2 ns: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.91 us: 1.03x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.2 ms: 1.05x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 91.8 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.69 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 541 ms: 1.05x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.9 ms: 1.06x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                     |
| pickle_list                | 2.83 us                                                     | 3.00 us: 1.06x slower                                                      |
| scimark_fft                | 184 ms                                                      | 196 ms: 1.06x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.37 ms: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                      |
| pyflate                    | 295 ms                                                      | 320 ms: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 892 us: 1.11x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.7 ms: 1.11x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.7 ms: 1.12x slower                                                      |
| richards_super             | 32.1 ms                                                     | 35.9 ms: 1.12x slower                                                      |
| pycparser                  | 699 ms                                                      | 786 ms: 1.13x slower                                                       |
| richards                   | 28.4 ms                                                     | 31.9 ms: 1.13x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.14x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 42.7 ns: 1.14x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 89.9 ms: 1.14x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.9 ms: 1.15x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                     |
| nbody                      | 71.9 ms                                                     | 83.7 ms: 1.16x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 883 us: 1.17x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.62 us: 1.18x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                       |
| fannkuch                   | 247 ms                                                      | 294 ms: 1.19x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.97 ms: 1.20x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (6): asyncio_tcp, coroutines, xml_etree_iterparse, gc_traversal, xml_etree_parse, json
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 87.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown