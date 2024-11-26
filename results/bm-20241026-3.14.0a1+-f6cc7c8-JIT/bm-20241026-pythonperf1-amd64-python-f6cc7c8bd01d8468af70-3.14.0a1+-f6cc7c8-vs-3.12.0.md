# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-amd64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.008x faster
- HPT reliability: 71.78%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 250 ms: 1.15x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.92 sec: 1.16x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 98.7 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                        |
| async_tree_io              | 731 ms                                                      | 539 ms: 1.36x faster                                                        |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 221 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 604 ms: 1.28x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 403 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.7 ms: 1.34x faster                                                       |
| float          | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 95.9 ms: 1.03x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.04x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 144 us: 1.08x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.18 ms: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.06 ms: 1.40x faster                                                       |
| django_template | 22.9 ms                                                     | 27.0 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 16.8 us: 1.41x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.06 ms: 1.40x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                        |
| async_tree_io              | 731 ms                                                      | 539 ms: 1.36x faster                                                        |
| nbody                      | 71.9 ms                                                     | 53.7 ms: 1.34x faster                                                       |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 221 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 604 ms: 1.28x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                                        |
| deepcopy                   | 238 us                                                      | 190 us: 1.26x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 403 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.23x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 64.9 ms: 1.21x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.20x faster                                                       |
| float                      | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.5 ms: 1.20x faster                                                       |
| scimark_fft                | 184 ms                                                      | 155 ms: 1.19x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.2 ms: 1.17x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 57.6 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.23 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.11x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 950 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 468 ms: 1.10x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.10x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.9 ms: 1.06x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 56.2 ms: 1.05x faster                                                       |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 58.4 ns: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| fannkuch                   | 247 ms                                                      | 240 ms: 1.03x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 839 us: 1.02x faster                                                        |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.63 us: 1.01x faster                                                       |
| pyflate                    | 295 ms                                                      | 292 ms: 1.01x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                       |
| pathlib                    | 80.5 ms                                                     | 81.2 ms: 1.01x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                       |
| generators                 | 22.5 ms                                                     | 22.9 ms: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.1 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 95.9 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 727 ms: 1.04x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.04x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| raytrace                   | 192 ms                                                      | 208 ms: 1.08x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 144 us: 1.08x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.18 ms: 1.09x slower                                                       |
| sympy_str                  | 175 ms                                                      | 191 ms: 1.09x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.53 ms: 1.10x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 886 us: 1.10x slower                                                        |
| tornado_http               | 89.5 ms                                                     | 98.7 ms: 1.10x slower                                                       |
| async_generators           | 239 ms                                                      | 267 ms: 1.11x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 210 ms: 1.12x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 103 ms: 1.12x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                       |
| 2to3                       | 218 ms                                                      | 250 ms: 1.15x slower                                                        |
| sympy_expand               | 284 ms                                                      | 326 ms: 1.15x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.18 ms: 1.15x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.92 sec: 1.16x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.0 ms: 1.18x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.63 sec: 1.18x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.5 ms: 1.20x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.4 ms: 1.21x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.7 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 42.9 ms: 1.24x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.95 ms: 1.28x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.26 ms: 1.28x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.3 ms: 1.29x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.41 ms: 1.87x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): meteor_contest, go, logging_simple
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 71.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown