# Results vs. base

- fork: faster-cpython
- ref: no_thresholds
- machine: linux-x86_64
- commit hash: a4985b2
- commit date: 2024-03-28
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 278 ms                                                                 | 281 ms: 1.01x slower                                                      |
| chameleon      | 6.89 ms                                                                | 7.06 ms: 1.03x slower                                                     |
| docutils       | 2.89 sec                                                               | 2.94 sec: 1.01x slower                                                    |
| html5lib       | 67.4 ms                                                                | 66.2 ms: 1.02x faster                                                     |
| tornado_http   | 96.8 ms                                                                | 97.6 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none | 390 ms                                                                 | 355 ms: 1.10x faster                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (7): async_tree_io, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 92.6 ms                                                                | 90.6 ms: 1.02x faster                                                     |
| pidigits       | 189 ms                                                                 | 190 ms: 1.00x slower                                                      |
| float          | 76.5 ms                                                                | 79.5 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.74 ms                                                                | 3.81 ms: 1.02x slower                                                     |
| regex_v8       | 25.5 ms                                                                | 26.2 ms: 1.03x slower                                                     |
| regex_dna      | 224 ms                                                                 | 231 ms: 1.03x slower                                                      |
| regex_compile  | 146 ms                                                                 | 151 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list        | 5.20 us                                                                | 5.04 us: 1.03x faster                                                     |
| json_loads           | 28.6 us                                                                | 28.3 us: 1.01x faster                                                     |
| pickle_list          | 4.99 us                                                                | 4.94 us: 1.01x faster                                                     |
| pickle_pure_python   | 308 us                                                                 | 306 us: 1.01x faster                                                      |
| pickle_dict          | 34.2 us                                                                | 34.0 us: 1.00x faster                                                     |
| pickle               | 11.8 us                                                                | 11.9 us: 1.01x slower                                                     |
| xml_etree_parse      | 159 ms                                                                 | 162 ms: 1.02x slower                                                      |
| xml_etree_process    | 61.3 ms                                                                | 62.8 ms: 1.03x slower                                                     |
| xml_etree_generate   | 88.6 ms                                                                | 91.9 ms: 1.04x slower                                                     |
| tomli_loads          | 2.06 sec                                                               | 2.15 sec: 1.04x slower                                                    |
| xml_etree_iterparse  | 107 ms                                                                 | 113 ms: 1.05x slower                                                      |
| unpickle_pure_python | 240 us                                                                 | 267 us: 1.11x slower                                                      |
| unpickle             | 15.0 us                                                                | 16.7 us: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                     |
| python_startup_no_site | 9.53 ms                                                                | 9.62 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 36.2 ms                                                                | 37.0 ms: 1.02x slower                                                     |
| genshi_text     | 25.3 ms                                                                | 25.9 ms: 1.03x slower                                                     |
| genshi_xml      | 54.6 ms                                                                | 57.0 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none          | 390 ms                                                                 | 355 ms: 1.10x faster                                                      |
| unpack_sequence          | 91.3 ns                                                                | 86.9 ns: 1.05x faster                                                     |
| unpickle_list            | 5.20 us                                                                | 5.04 us: 1.03x faster                                                     |
| nbody                    | 92.6 ms                                                                | 90.6 ms: 1.02x faster                                                     |
| html5lib                 | 67.4 ms                                                                | 66.2 ms: 1.02x faster                                                     |
| scimark_sparse_mat_mult  | 4.87 ms                                                                | 4.79 ms: 1.02x faster                                                     |
| json_loads               | 28.6 us                                                                | 28.3 us: 1.01x faster                                                     |
| pickle_list              | 4.99 us                                                                | 4.94 us: 1.01x faster                                                     |
| gunicorn                 | 1.32 ms                                                                | 1.30 ms: 1.01x faster                                                     |
| pickle_pure_python       | 308 us                                                                 | 306 us: 1.01x faster                                                      |
| spectral_norm            | 115 ms                                                                 | 114 ms: 1.01x faster                                                      |
| scimark_lu               | 133 ms                                                                 | 132 ms: 1.01x faster                                                      |
| pickle_dict              | 34.2 us                                                                | 34.0 us: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.86 sec                                                               | 1.85 sec: 1.00x faster                                                    |
| pidigits                 | 189 ms                                                                 | 190 ms: 1.00x slower                                                      |
| python_startup           | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                     |
| tornado_http             | 96.8 ms                                                                | 97.6 ms: 1.01x slower                                                     |
| python_startup_no_site   | 9.53 ms                                                                | 9.62 ms: 1.01x slower                                                     |
| 2to3                     | 278 ms                                                                 | 281 ms: 1.01x slower                                                      |
| pickle                   | 11.8 us                                                                | 11.9 us: 1.01x slower                                                     |
| pathlib                  | 19.0 ms                                                                | 19.2 ms: 1.01x slower                                                     |
| coverage                 | 96.3 ms                                                                | 97.5 ms: 1.01x slower                                                     |
| telco                    | 8.58 ms                                                                | 8.68 ms: 1.01x slower                                                     |
| dulwich_log              | 70.6 ms                                                                | 71.5 ms: 1.01x slower                                                     |
| sympy_sum                | 166 ms                                                                 | 168 ms: 1.01x slower                                                      |
| json                     | 5.36 ms                                                                | 5.43 ms: 1.01x slower                                                     |
| sympy_expand             | 491 ms                                                                 | 498 ms: 1.01x slower                                                      |
| docutils                 | 2.89 sec                                                               | 2.94 sec: 1.01x slower                                                    |
| xml_etree_parse          | 159 ms                                                                 | 162 ms: 1.02x slower                                                      |
| thrift                   | 806 us                                                                 | 819 us: 1.02x slower                                                      |
| logging_simple           | 5.92 us                                                                | 6.01 us: 1.02x slower                                                     |
| logging_silent           | 102 ns                                                                 | 104 ns: 1.02x slower                                                      |
| sqlglot_normalize        | 113 ms                                                                 | 115 ms: 1.02x slower                                                      |
| meteor_contest           | 110 ms                                                                 | 112 ms: 1.02x slower                                                      |
| regex_effbot             | 3.74 ms                                                                | 3.81 ms: 1.02x slower                                                     |
| sympy_str                | 289 ms                                                                 | 295 ms: 1.02x slower                                                      |
| sqlglot_transpile        | 1.65 ms                                                                | 1.69 ms: 1.02x slower                                                     |
| sqlglot_parse            | 1.34 ms                                                                | 1.36 ms: 1.02x slower                                                     |
| gc_traversal             | 3.69 ms                                                                | 3.77 ms: 1.02x slower                                                     |
| create_gc_cycles         | 1.66 ms                                                                | 1.70 ms: 1.02x slower                                                     |
| django_template          | 36.2 ms                                                                | 37.0 ms: 1.02x slower                                                     |
| pycparser                | 1.23 sec                                                               | 1.26 sec: 1.02x slower                                                    |
| coroutines               | 22.6 ms                                                                | 23.1 ms: 1.02x slower                                                     |
| genshi_text              | 25.3 ms                                                                | 25.9 ms: 1.03x slower                                                     |
| sympy_integrate          | 21.8 ms                                                                | 22.4 ms: 1.03x slower                                                     |
| chameleon                | 6.89 ms                                                                | 7.06 ms: 1.03x slower                                                     |
| xml_etree_process        | 61.3 ms                                                                | 62.8 ms: 1.03x slower                                                     |
| regex_v8                 | 25.5 ms                                                                | 26.2 ms: 1.03x slower                                                     |
| raytrace                 | 294 ms                                                                 | 302 ms: 1.03x slower                                                      |
| logging_format           | 6.54 us                                                                | 6.73 us: 1.03x slower                                                     |
| chaos                    | 63.4 ms                                                                | 65.3 ms: 1.03x slower                                                     |
| sqlglot_optimize         | 57.6 ms                                                                | 59.4 ms: 1.03x slower                                                     |
| regex_dna                | 224 ms                                                                 | 231 ms: 1.03x slower                                                      |
| fannkuch                 | 388 ms                                                                 | 400 ms: 1.03x slower                                                      |
| regex_compile            | 146 ms                                                                 | 151 ms: 1.03x slower                                                      |
| deepcopy_reduce          | 3.17 us                                                                | 3.28 us: 1.04x slower                                                     |
| typing_runtime_protocols | 111 us                                                                 | 116 us: 1.04x slower                                                      |
| bench_thread_pool        | 858 us                                                                 | 890 us: 1.04x slower                                                      |
| xml_etree_generate       | 88.6 ms                                                                | 91.9 ms: 1.04x slower                                                     |
| float                    | 76.5 ms                                                                | 79.5 ms: 1.04x slower                                                     |
| pprint_safe_repr         | 741 ms                                                                 | 772 ms: 1.04x slower                                                      |
| genshi_xml               | 54.6 ms                                                                | 57.0 ms: 1.04x slower                                                     |
| deepcopy                 | 359 us                                                                 | 375 us: 1.04x slower                                                      |
| mdp                      | 2.65 sec                                                               | 2.77 sec: 1.04x slower                                                    |
| tomli_loads              | 2.06 sec                                                               | 2.15 sec: 1.04x slower                                                    |
| pprint_pformat           | 1.52 sec                                                               | 1.58 sec: 1.05x slower                                                    |
| xml_etree_iterparse      | 107 ms                                                                 | 113 ms: 1.05x slower                                                      |
| scimark_monte_carlo      | 70.7 ms                                                                | 74.8 ms: 1.06x slower                                                     |
| comprehensions           | 18.3 us                                                                | 19.5 us: 1.07x slower                                                     |
| async_generators         | 457 ms                                                                 | 493 ms: 1.08x slower                                                      |
| go                       | 156 ms                                                                 | 173 ms: 1.11x slower                                                      |
| unpickle_pure_python     | 240 us                                                                 | 267 us: 1.11x slower                                                      |
| richards_super           | 52.6 ms                                                                | 58.6 ms: 1.11x slower                                                     |
| unpickle                 | 15.0 us                                                                | 16.7 us: 1.12x slower                                                     |
| nqueens                  | 91.9 ms                                                                | 104 ms: 1.13x slower                                                      |
| richards                 | 46.7 ms                                                                | 52.9 ms: 1.13x slower                                                     |
| hexiom                   | 7.12 ms                                                                | 8.09 ms: 1.14x slower                                                     |
| deepcopy_memo            | 38.9 us                                                                | 44.9 us: 1.16x slower                                                     |
| deltablue                | 3.50 ms                                                                | 4.14 ms: 1.18x slower                                                     |
| Geometric mean           | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (23): async_tree_io, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, aiohttp, djangocms, bench_mp_pool, scimark_fft, json_dumps, scimark_sor, asyncio_websockets, asyncio_tcp, dask, pyflate, sqlite_synth, generators, mako, crypto_pyaes, mypy2, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, pylint


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.01x