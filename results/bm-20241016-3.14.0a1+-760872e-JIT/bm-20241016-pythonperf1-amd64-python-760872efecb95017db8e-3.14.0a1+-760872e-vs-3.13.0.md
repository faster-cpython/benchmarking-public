# Results vs. 3.13.0

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-amd64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.04x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 247 ms: 1.14x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.91 sec: 1.21x slower                                                      |
| html5lib       | 38.6 ms                                                     | 39.7 ms: 1.03x slower                                                       |
| tornado_http   | 92.8 ms                                                     | 98.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                        |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.53 sec: 1.07x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 209 ms: 1.01x slower                                                        |
| async_tree_none            | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| async_tree_io              | 521 ms                                                      | 554 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                        |
| async_tree_io_tg           | 512 ms                                                      | 635 ms: 1.24x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_memoization, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 54.7 ms: 1.18x faster                                                       |
| float          | 48.1 ms                                                     | 47.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.65 ms: 1.02x slower                                                       |
| regex_v8       | 14.7 ms                                                     | 15.6 ms: 1.06x slower                                                       |
| regex_dna      | 114 ms                                                      | 123 ms: 1.07x slower                                                        |
| regex_compile  | 80.1 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                      |
| pickle_list          | 2.89 us                                                     | 2.71 us: 1.07x faster                                                       |
| xml_etree_generate   | 53.3 ms                                                     | 51.1 ms: 1.04x faster                                                       |
| pickle_dict          | 18.0 us                                                     | 17.6 us: 1.02x faster                                                       |
| pickle               | 7.34 us                                                     | 7.21 us: 1.02x faster                                                       |
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                     | 62.9 ms: 1.01x slower                                                       |
| xml_etree_parse      | 93.2 ms                                                     | 95.6 ms: 1.03x slower                                                       |
| unpickle             | 8.63 us                                                     | 9.04 us: 1.05x slower                                                       |
| unpickle_list        | 2.72 us                                                     | 2.87 us: 1.05x slower                                                       |
| pickle_pure_python   | 183 us                                                      | 197 us: 1.07x slower                                                        |
| json_dumps           | 5.76 ms                                                     | 6.37 ms: 1.11x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 142 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                       |
| python_startup         | 22.2 ms                                                     | 23.9 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 4.94 ms: 1.26x faster                                                       |
| django_template | 21.8 ms                                                     | 27.0 ms: 1.24x slower                                                       |
| genshi_text     | 14.9 ms                                                     | 19.6 ms: 1.32x slower                                                       |
| genshi_xml      | 32.8 ms                                                     | 46.3 ms: 1.41x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 513 us: 16.90x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 16.4 us: 1.33x faster                                                       |
| mako                       | 6.24 ms                                                     | 4.94 ms: 1.26x faster                                                       |
| nbody                      | 64.5 ms                                                     | 54.7 ms: 1.18x faster                                                       |
| deepcopy                   | 223 us                                                      | 192 us: 1.16x faster                                                        |
| scimark_fft                | 174 ms                                                      | 154 ms: 1.13x faster                                                        |
| scimark_sor                | 72.0 ms                                                     | 64.0 ms: 1.12x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.34 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 36.1 ms: 1.12x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                        |
| spectral_norm              | 59.2 ms                                                     | 54.5 ms: 1.09x faster                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 39.8 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.08x faster                                                       |
| pprint_safe_repr           | 493 ms                                                      | 458 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.18 ms: 1.07x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.53 sec: 1.07x faster                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                      |
| pickle_list                | 2.89 us                                                     | 2.71 us: 1.07x faster                                                       |
| pprint_pformat             | 991 ms                                                      | 935 ms: 1.06x faster                                                        |
| fannkuch                   | 245 ms                                                      | 231 ms: 1.06x faster                                                        |
| xml_etree_generate         | 53.3 ms                                                     | 51.1 ms: 1.04x faster                                                       |
| pickle_dict                | 18.0 us                                                     | 17.6 us: 1.02x faster                                                       |
| pickle                     | 7.34 us                                                     | 7.21 us: 1.02x faster                                                       |
| float                      | 48.1 ms                                                     | 47.5 ms: 1.01x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 80.5 ms: 1.01x faster                                                       |
| json_loads                 | 14.3 us                                                     | 14.2 us: 1.01x faster                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 62.9 ms: 1.01x slower                                                       |
| json                       | 2.98 ms                                                     | 3.01 ms: 1.01x slower                                                       |
| async_tree_none_tg         | 206 ms                                                      | 209 ms: 1.01x slower                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.65 ms: 1.02x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 55.4 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.2 ms                                                     | 95.6 ms: 1.03x slower                                                       |
| coverage                   | 46.7 ms                                                     | 48.0 ms: 1.03x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 39.7 ms: 1.03x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 75.5 ms: 1.05x slower                                                       |
| unpickle                   | 8.63 us                                                     | 9.04 us: 1.05x slower                                                       |
| async_tree_none            | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| pyflate                    | 275 ms                                                      | 289 ms: 1.05x slower                                                        |
| unpickle_list              | 2.72 us                                                     | 2.87 us: 1.05x slower                                                       |
| tornado_http               | 92.8 ms                                                     | 98.1 ms: 1.06x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 15.6 ms: 1.06x slower                                                       |
| async_tree_io              | 521 ms                                                      | 554 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                        |
| regex_dna                  | 114 ms                                                      | 123 ms: 1.07x slower                                                        |
| pickle_pure_python         | 183 us                                                      | 197 us: 1.07x slower                                                        |
| logging_format             | 6.15 us                                                     | 6.62 us: 1.08x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.17 us: 1.08x slower                                                       |
| python_startup             | 22.2 ms                                                     | 23.9 ms: 1.08x slower                                                       |
| go                         | 84.6 ms                                                     | 91.2 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.7 ms: 1.10x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.37 ms: 1.11x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 56.5 ns: 1.11x slower                                                       |
| comprehensions             | 10.2 us                                                     | 11.4 us: 1.11x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 142 us: 1.12x slower                                                        |
| mdp                        | 1.38 sec                                                    | 1.56 sec: 1.12x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 113 us: 1.13x slower                                                        |
| 2to3                       | 217 ms                                                      | 247 ms: 1.14x slower                                                        |
| sympy_expand               | 285 ms                                                      | 325 ms: 1.14x slower                                                        |
| regex_compile              | 80.1 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 63.5 ms: 1.14x slower                                                       |
| sympy_str                  | 166 ms                                                      | 192 ms: 1.16x slower                                                        |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                        |
| sqlglot_parse              | 761 us                                                      | 897 us: 1.18x slower                                                        |
| generators                 | 19.5 ms                                                     | 23.0 ms: 1.18x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 103 ms: 1.19x slower                                                        |
| sqlglot_normalize          | 171 ms                                                      | 207 ms: 1.21x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.91 sec: 1.21x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.18 ms: 1.24x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 635 ms: 1.24x slower                                                        |
| django_template            | 21.8 ms                                                     | 27.0 ms: 1.24x slower                                                       |
| gc_traversal               | 1.55 ms                                                     | 1.96 ms: 1.26x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.37 ms: 1.27x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 15.8 ms: 1.28x slower                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 89.8 ms: 1.29x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 43.2 ms: 1.31x slower                                                       |
| richards                   | 26.0 ms                                                     | 34.0 ms: 1.31x slower                                                       |
| richards_super             | 29.3 ms                                                     | 38.5 ms: 1.31x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 19.6 ms: 1.32x slower                                                       |
| pylint                     | 211 ms                                                      | 279 ms: 1.32x slower                                                        |
| raytrace                   | 156 ms                                                      | 215 ms: 1.38x slower                                                        |
| hexiom                     | 3.69 ms                                                     | 5.21 ms: 1.41x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 46.3 ms: 1.41x slower                                                       |
| unpack_sequence            | 40.0 ns                                                     | 59.3 ns: 1.48x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 1.41 ms: 1.70x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (9): pycparser, sqlite_synth, bench_thread_pool, pidigits, xml_etree_process, async_tree_cpu_io_mixed, dulwich_log, async_tree_memoization, asyncio_tcp
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: sphinx

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown