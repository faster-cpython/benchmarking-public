# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-amd64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.039x faster
- HPT reliability: 94.08%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.80 sec: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                        |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 575 ms: 1.34x faster                                                        |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 273 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 414 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 410 ms: 1.19x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.8 ms: 1.42x faster                                                       |
| float          | 56.8 ms                                                     | 47.7 ms: 1.19x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 85.2 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.23x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 52.5 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 95.3 ms: 1.02x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.45 ms: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.19 ms: 1.37x faster                                                       |
| django_template | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 16.1 us: 1.47x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                        |
| nbody                      | 71.9 ms                                                     | 50.8 ms: 1.42x faster                                                       |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.19 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 575 ms: 1.34x faster                                                        |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 273 ms: 1.24x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.23x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 64.4 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 414 ms: 1.21x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.1 ms: 1.21x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 55.4 ms: 1.21x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.20x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.5 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 410 ms: 1.19x faster                                                        |
| float                      | 56.8 ms                                                     | 47.7 ms: 1.19x faster                                                       |
| scimark_fft                | 184 ms                                                      | 157 ms: 1.18x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.23 ms: 1.15x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 52.2 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 40.2 ms: 1.10x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 958 ms: 1.09x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 472 ms: 1.09x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 74.1 ms: 1.09x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.4 ms: 1.07x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.5 ms: 1.06x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 58.0 ns: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 824 us: 1.04x faster                                                        |
| pyflate                    | 295 ms                                                      | 285 ms: 1.03x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 72.2 ms: 1.03x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 85.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.14 us: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 89.6 ms: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.61 us: 1.02x faster                                                       |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 95.3 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 94.7 ms: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                       |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 65.4 ms: 1.04x slower                                                       |
| fannkuch                   | 247 ms                                                      | 257 ms: 1.04x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.40 ms: 1.07x slower                                                       |
| raytrace                   | 192 ms                                                      | 205 ms: 1.07x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.9 ms: 1.08x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.33 ms: 1.08x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 871 us: 1.08x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.80 sec: 1.09x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.10x slower                                                       |
| sympy_expand               | 284 ms                                                      | 312 ms: 1.10x slower                                                        |
| async_generators           | 239 ms                                                      | 266 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 38.3 ms: 1.11x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 211 ms: 1.13x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.45 ms: 1.13x slower                                                       |
| richards                   | 28.4 ms                                                     | 32.4 ms: 1.14x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.8 ms: 1.15x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.6 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 82.1 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.86 ms: 1.22x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.03 ms: 1.23x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.75x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): generators
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 94.08% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown