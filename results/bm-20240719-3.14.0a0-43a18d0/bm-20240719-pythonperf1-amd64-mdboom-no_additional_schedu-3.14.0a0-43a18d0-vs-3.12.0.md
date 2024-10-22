# Results vs. 3.12.0

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 43a18d0
- commit date: 2024-07-19
- overall geometric mean: 1.00x faster
- HPT reliability: 98.70%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 91.8 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 246 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 193 ms: 1.48x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 538 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                       |
| async_tree_io              | 731 ms                                                      | 546 ms: 1.34x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| nbody          | 71.9 ms                                                     | 77.8 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 89.7 ms: 1.02x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.2 ms: 1.01x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 58.3 ms: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.13 ms: 1.08x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.3 ms: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 152 us: 1.14x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.5 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| mako            | 7.09 ms                                                     | 7.52 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 246 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 193 ms: 1.48x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 538 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                       |
| async_tree_io              | 731 ms                                                      | 546 ms: 1.34x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                       |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.70 sec: 1.23x faster                                                     |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.4 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                      |
| raytrace                   | 192 ms                                                      | 176 ms: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.7 us: 1.09x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 800 us: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.2 ms: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.2 ms: 1.03x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 67.6 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.23 us: 1.01x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 75.5 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.2 ms: 1.01x slower                                                      |
| go                         | 91.6 ms                                                     | 93.0 ms: 1.02x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.1 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| regex_compile              | 87.5 ms                                                     | 89.7 ms: 1.02x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 91.8 ms: 1.03x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.04x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.7 ns: 1.04x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 58.3 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| sympy_expand               | 284 ms                                                      | 298 ms: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 51.2 ms: 1.06x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 83.2 ms: 1.06x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.34 ms: 1.06x slower                                                      |
| pyflate                    | 295 ms                                                      | 313 ms: 1.06x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 517 ms: 1.06x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.52 ms: 1.06x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.08x slower                                                     |
| spectral_norm              | 66.9 ms                                                     | 72.0 ms: 1.08x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.13 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                      |
| nbody                      | 71.9 ms                                                     | 77.8 ms: 1.08x slower                                                      |
| richards_super             | 32.1 ms                                                     | 34.8 ms: 1.08x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 557 ms: 1.09x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.8 ms: 1.09x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.3 ms: 1.09x slower                                                      |
| coverage                   | 40.8 ms                                                     | 44.9 ms: 1.10x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.5 ms: 1.10x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 891 us: 1.11x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.84 ms: 1.11x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.6 ms: 1.11x slower                                                      |
| scimark_fft                | 184 ms                                                      | 207 ms: 1.12x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 67.2 ms: 1.14x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 152 us: 1.14x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                       |
| fannkuch                   | 247 ms                                                      | 290 ms: 1.18x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.86 ms: 1.18x slower                                                      |
| pycparser                  | 699 ms                                                      | 830 ms: 1.19x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 897 us: 1.19x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (5): float, chaos, sqlglot_normalize, pathlib, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240719-3.14.0a0-43a18d0/bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.70% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown