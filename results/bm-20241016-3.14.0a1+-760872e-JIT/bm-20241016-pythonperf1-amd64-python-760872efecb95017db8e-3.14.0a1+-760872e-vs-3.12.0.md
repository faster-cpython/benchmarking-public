# Results vs. 3.12.0

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-amd64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.01x faster
- HPT reliability: 76.84%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 247 ms: 1.13x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 98.1 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                                        |
| async_tree_io              | 731 ms                                                      | 554 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.25x faster                                                        |
| async_tree_none            | 291 ms                                                      | 234 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 635 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.7 ms: 1.31x faster                                                       |
| float          | 56.8 ms                                                     | 47.5 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.65 ms: 1.02x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.6 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.04x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.71 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                       |
| pickle               | 7.43 us                                                     | 7.21 us: 1.03x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 197 us: 1.01x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 95.6 ms: 1.03x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.87 us: 1.04x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.06x slower                                                        |
| unpickle             | 8.18 us                                                     | 9.04 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.37 ms: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.9 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.94 ms: 1.43x faster                                                       |
| django_template | 22.9 ms                                                     | 27.0 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 16.4 us: 1.45x faster                                                       |
| mako                       | 7.09 ms                                                     | 4.94 ms: 1.43x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.53 sec: 1.37x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                                        |
| async_tree_io              | 731 ms                                                      | 554 ms: 1.32x faster                                                        |
| nbody                      | 71.9 ms                                                     | 54.7 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.25x faster                                                        |
| async_tree_none            | 291 ms                                                      | 234 ms: 1.25x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                       |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 64.0 ms: 1.23x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 54.5 ms: 1.23x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 39.8 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 635 ms: 1.21x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.1 ms: 1.21x faster                                                       |
| scimark_fft                | 184 ms                                                      | 154 ms: 1.20x faster                                                        |
| float                      | 56.8 ms                                                     | 47.5 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.18 ms: 1.17x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 458 ms: 1.12x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 935 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.10x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.10x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.5 ns: 1.07x faster                                                       |
| fannkuch                   | 247 ms                                                      | 231 ms: 1.07x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 55.4 ms: 1.06x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.04x faster                                                       |
| pickle_list                | 2.83 us                                                     | 2.71 us: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 827 us: 1.04x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                       |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.03x faster                                                        |
| pickle                     | 7.43 us                                                     | 7.21 us: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| pyflate                    | 295 ms                                                      | 289 ms: 1.02x faster                                                        |
| logging_simple             | 6.28 us                                                     | 6.17 us: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.62 us: 1.01x faster                                                       |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 197 us: 1.01x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 63.5 ms: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.5 ms: 1.01x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.65 ms: 1.02x slower                                                       |
| generators                 | 22.5 ms                                                     | 23.0 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 95.6 ms: 1.03x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.87 us: 1.04x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.34 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.06x slower                                                        |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                                        |
| async_generators           | 239 ms                                                      | 260 ms: 1.08x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.6 ms: 1.09x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 98.1 ms: 1.10x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                       |
| sympy_str                  | 175 ms                                                      | 192 ms: 1.10x slower                                                        |
| unpickle                   | 8.18 us                                                     | 9.04 us: 1.10x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 207 ms: 1.11x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 897 us: 1.12x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.37 ms: 1.12x slower                                                       |
| raytrace                   | 192 ms                                                      | 215 ms: 1.12x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 103 ms: 1.13x slower                                                        |
| 2to3                       | 218 ms                                                      | 247 ms: 1.13x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.56 sec: 1.13x slower                                                      |
| sympy_expand               | 284 ms                                                      | 325 ms: 1.14x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.18 ms: 1.15x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.0 ms: 1.18x slower                                                       |
| django_template            | 22.9 ms                                                     | 27.0 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                        |
| richards_super             | 32.1 ms                                                     | 38.5 ms: 1.20x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.0 ms: 1.20x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.8 ms: 1.22x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.9 ms: 1.23x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 43.2 ms: 1.25x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.21 ms: 1.27x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.8 ms: 1.30x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 665 ms: 1.36x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 59.3 ns: 1.58x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.41 ms: 1.87x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): go, pathlib
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 76.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown