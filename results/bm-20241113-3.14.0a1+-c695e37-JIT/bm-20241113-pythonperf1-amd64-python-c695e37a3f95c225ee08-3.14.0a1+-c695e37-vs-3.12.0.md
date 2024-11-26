# Results vs. 3.12.0

- fork: python
- ref: c695e37a3f95c225ee08
- machine: windows-amd64
- commit hash: c695e37
- commit date: 2024-11-13
- overall geometric mean: 1.020x faster
- HPT reliability: 89.46%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 245 ms: 1.12x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                        |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.40x faster                                                        |
| async_tree_io              | 731 ms                                                      | 553 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 219 ms: 1.30x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 630 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                       |
| float          | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 90.2 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 51.0 ms: 1.09x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.4 ms: 1.04x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.06x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.11x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.38 ms: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.18 ms: 1.37x faster                                                       |
| django_template | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 16.2 us: 1.47x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                        |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.40x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.18 ms: 1.37x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                       |
| async_tree_io              | 731 ms                                                      | 553 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 219 ms: 1.30x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.29x faster                                                        |
| deepcopy                   | 238 us                                                      | 186 us: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 64.1 ms: 1.23x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 39.6 ms: 1.23x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 630 ms: 1.22x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 55.4 ms: 1.21x faster                                                       |
| float                      | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| scimark_fft                | 184 ms                                                      | 155 ms: 1.19x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.18x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.9 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.22 ms: 1.15x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 452 ms: 1.14x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 924 ms: 1.13x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.8 ms: 1.11x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.6 ns: 1.11x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.0 ms: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 54.2 ms: 1.09x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 74.9 ms: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.4 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.4 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 822 us: 1.04x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.10 us: 1.03x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.56 us: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.9 ms: 1.02x faster                                                       |
| fannkuch                   | 247 ms                                                      | 243 ms: 1.02x faster                                                        |
| go                         | 91.6 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| generators                 | 22.5 ms                                                     | 22.8 ms: 1.01x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 718 ms: 1.03x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 90.2 ms: 1.03x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.7 ms: 1.05x slower                                                       |
| pyflate                    | 295 ms                                                      | 313 ms: 1.06x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.06x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.43 ms: 1.07x slower                                                       |
| sympy_str                  | 175 ms                                                      | 190 ms: 1.08x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.36 ms: 1.09x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.11x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 102 ms: 1.11x slower                                                        |
| async_generators           | 239 ms                                                      | 267 ms: 1.12x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 899 us: 1.12x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.38 ms: 1.12x slower                                                       |
| 2to3                       | 218 ms                                                      | 245 ms: 1.12x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 210 ms: 1.13x slower                                                        |
| sympy_expand               | 284 ms                                                      | 322 ms: 1.14x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.18 ms: 1.16x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                                       |
| raytrace                   | 192 ms                                                      | 225 ms: 1.17x slower                                                        |
| coverage                   | 40.8 ms                                                     | 47.8 ms: 1.17x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.6 ms: 1.20x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.4 ms: 1.23x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 117 us: 1.23x slower                                                        |
| richards                   | 28.4 ms                                                     | 35.2 ms: 1.24x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 42.9 ms: 1.24x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 86.7 ms: 1.25x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.91 ms: 1.26x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.19 ms: 1.27x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.83x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241113-3.14.0a1+-c695e37-JIT/bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 89.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown