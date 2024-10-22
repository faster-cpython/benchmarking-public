# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.09x slower
- HPT reliability: 64.60%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 314 ms: 1.08x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.7 ms: 1.02x faster                                                       |
| tornado_http   | 120 ms                                                       | 123 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 377 ms: 1.22x faster                                                        |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 412 ms: 1.10x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 321 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.03x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 378 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| async_tree_io_tg           | 819 ms                                                       | 863 ms: 1.05x slower                                                        |
| async_generators           | 359 ms                                                       | 388 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                       |
| float          | 81.9 ms                                                      | 79.3 ms: 1.03x faster                                                       |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 247 ms: 1.01x slower                                                        |
| regex_v8       | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| regex_compile  | 144 ms                                                       | 152 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.15 sec: 1.12x faster                                                      |
| xml_etree_generate   | 85.3 ms                                                      | 82.0 ms: 1.04x faster                                                       |
| xml_etree_process    | 60.9 ms                                                      | 58.6 ms: 1.04x faster                                                       |
| pickle_dict          | 32.1 us                                                      | 31.7 us: 1.01x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| unpickle_list        | 4.62 us                                                      | 4.67 us: 1.01x slower                                                       |
| pickle               | 10.5 us                                                      | 10.7 us: 1.01x slower                                                       |
| json_loads           | 24.0 us                                                      | 24.3 us: 1.01x slower                                                       |
| unpickle             | 15.1 us                                                      | 15.4 us: 1.02x slower                                                       |
| json_dumps           | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 226 us: 1.06x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 337 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                                       |
| python_startup         | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.39 ms: 1.11x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 28.3 ms: 1.06x slower                                                       |
| django_template | 38.9 ms                                                      | 43.9 ms: 1.13x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 65.1 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 29.9 us: 1.32x faster                                                       |
| deepcopy                   | 397 us                                                       | 313 us: 1.27x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 377 ms: 1.22x faster                                                        |
| richards_super             | 59.8 ms                                                      | 48.9 ms: 1.22x faster                                                       |
| scimark_sor                | 126 ms                                                       | 103 ms: 1.22x faster                                                        |
| richards                   | 52.7 ms                                                      | 43.7 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.11 us: 1.14x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.15 sec: 1.12x faster                                                      |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                                        |
| telco                      | 8.58 ms                                                      | 7.73 ms: 1.11x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.39 ms: 1.11x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 412 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| scimark_fft                | 314 ms                                                       | 291 ms: 1.08x faster                                                        |
| logging_silent             | 97.7 ns                                                      | 90.8 ns: 1.08x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.77 sec: 1.07x faster                                                      |
| go                         | 160 ms                                                       | 151 ms: 1.06x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 321 ms: 1.06x faster                                                        |
| nbody                      | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                       |
| pyflate                    | 492 ms                                                       | 467 ms: 1.05x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 92.8 ms: 1.05x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 93.9 ms: 1.04x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 82.0 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 58.6 ms: 1.04x faster                                                       |
| float                      | 81.9 ms                                                      | 79.3 ms: 1.03x faster                                                       |
| deltablue                  | 3.41 ms                                                      | 3.31 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.03x faster                                                        |
| json                       | 5.22 ms                                                      | 5.10 ms: 1.03x faster                                                       |
| dulwich_log                | 65.5 ms                                                      | 64.4 ms: 1.02x faster                                                       |
| html5lib                   | 71.9 ms                                                      | 70.7 ms: 1.02x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 71.5 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.79 us                                                      | 2.74 us: 1.02x faster                                                       |
| pickle_dict                | 32.1 us                                                      | 31.7 us: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 378 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 807 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| logging_format             | 7.07 us                                                      | 7.14 us: 1.01x slower                                                       |
| unpickle_list              | 4.62 us                                                      | 4.67 us: 1.01x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.01x slower                                                       |
| regex_dna                  | 244 ms                                                       | 247 ms: 1.01x slower                                                        |
| json_loads                 | 24.0 us                                                      | 24.3 us: 1.01x slower                                                       |
| unpickle                   | 15.1 us                                                      | 15.4 us: 1.02x slower                                                       |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| json_dumps                 | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                                       |
| tornado_http               | 120 ms                                                       | 123 ms: 1.02x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| thrift                     | 877 us                                                       | 899 us: 1.03x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 178 us: 1.03x slower                                                        |
| mdp                        | 2.52 sec                                                     | 2.60 sec: 1.03x slower                                                      |
| logging_simple             | 6.40 us                                                      | 6.63 us: 1.04x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.47 ms: 1.04x slower                                                       |
| regex_compile              | 144 ms                                                       | 152 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 863 ms: 1.05x slower                                                        |
| unpickle_pure_python       | 214 us                                                       | 226 us: 1.06x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 952 us: 1.06x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 337 us: 1.06x slower                                                        |
| sympy_expand               | 505 ms                                                       | 534 ms: 1.06x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 28.3 ms: 1.06x slower                                                       |
| raytrace                   | 289 ms                                                       | 307 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 69.6 ms: 1.07x slower                                                       |
| async_generators           | 359 ms                                                       | 388 ms: 1.08x slower                                                        |
| 2to3                       | 291 ms                                                       | 314 ms: 1.08x slower                                                        |
| chaos                      | 61.7 ms                                                      | 67.0 ms: 1.09x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.9 us: 1.09x slower                                                       |
| sympy_str                  | 296 ms                                                       | 324 ms: 1.09x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.52 ms: 1.10x slower                                                       |
| python_startup             | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 2.01 ms: 1.13x slower                                                       |
| django_template            | 38.9 ms                                                      | 43.9 ms: 1.13x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 7.16 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 134 ms: 1.13x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 65.1 ms: 1.14x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                      |
| generators                 | 33.5 ms                                                      | 38.3 ms: 1.14x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 176 ms: 1.15x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 103 ms: 1.17x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 70.3 ms: 1.18x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 27.6 ms: 1.18x slower                                                       |
| pylint                     | 346 ms                                                       | 422 ms: 1.22x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 5.21 ms: 1.27x slower                                                       |
| unpack_sequence            | 56.8 ns                                                      | 91.3 ns: 1.61x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.89 ms: 1.64x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 3.16 sec: 679.30x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                |

Benchmark hidden because not significant (8): async_tree_io, asyncio_websockets, fannkuch, xml_etree_iterparse, pprint_pformat, pickle_list, pycparser, coverage
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: sphinx

# HPT report

- Reliability score: 64.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x