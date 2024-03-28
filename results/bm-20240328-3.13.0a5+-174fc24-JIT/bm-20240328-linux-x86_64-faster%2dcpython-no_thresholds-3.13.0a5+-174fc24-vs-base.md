# Results vs. base

- fork: faster-cpython
- ref: no_thresholds
- machine: linux-x86_64
- commit hash: 174fc24
- commit date: 2024-03-28
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 278 ms                                                                 | 280 ms: 1.01x slower                                                      |
| chameleon      | 6.89 ms                                                                | 7.16 ms: 1.04x slower                                                     |
| docutils       | 2.89 sec                                                               | 2.93 sec: 1.01x slower                                                    |
| html5lib       | 67.4 ms                                                                | 66.4 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none  | 390 ms                                                                 | 360 ms: 1.09x faster                                                      |
| async_tree_io_tg | 930 ms                                                                 | 909 ms: 1.02x faster                                                      |
| Geometric mean   | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.5 ms                                                                | 79.6 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                                | 25.7 ms: 1.01x slower                                                     |
| regex_effbot   | 3.74 ms                                                                | 3.78 ms: 1.01x slower                                                     |
| regex_compile  | 146 ms                                                                 | 151 ms: 1.03x slower                                                      |
| regex_dna      | 224 ms                                                                 | 234 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                                | 10.7 ms: 1.01x slower                                                     |
| xml_etree_process    | 61.3 ms                                                                | 62.6 ms: 1.02x slower                                                     |
| pickle_list          | 4.99 us                                                                | 5.12 us: 1.03x slower                                                     |
| pickle               | 11.8 us                                                                | 12.1 us: 1.03x slower                                                     |
| tomli_loads          | 2.06 sec                                                               | 2.13 sec: 1.04x slower                                                    |
| xml_etree_iterparse  | 107 ms                                                                 | 112 ms: 1.05x slower                                                      |
| xml_etree_generate   | 88.6 ms                                                                | 92.9 ms: 1.05x slower                                                     |
| pickle_dict          | 34.2 us                                                                | 36.5 us: 1.07x slower                                                     |
| unpickle_pure_python | 240 us                                                                 | 268 us: 1.12x slower                                                      |
| unpickle             | 15.0 us                                                                | 17.1 us: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (4): unpickle_list, json_loads, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 11.1 ms                                                                | 11.1 ms: 1.00x faster                                                     |
| python_startup_no_site | 9.53 ms                                                                | 9.54 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                                | 10.8 ms: 1.01x slower                                                     |
| genshi_text     | 25.3 ms                                                                | 25.8 ms: 1.02x slower                                                     |
| django_template | 36.2 ms                                                                | 37.1 ms: 1.03x slower                                                     |
| genshi_xml      | 54.6 ms                                                                | 57.3 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5+-6c8ac8a | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none          | 390 ms                                                                 | 360 ms: 1.09x faster                                                      |
| unpack_sequence          | 91.3 ns                                                                | 88.0 ns: 1.04x faster                                                     |
| async_tree_io_tg         | 930 ms                                                                 | 909 ms: 1.02x faster                                                      |
| html5lib                 | 67.4 ms                                                                | 66.4 ms: 1.02x faster                                                     |
| scimark_lu               | 133 ms                                                                 | 132 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult  | 4.87 ms                                                                | 4.84 ms: 1.01x faster                                                     |
| spectral_norm            | 115 ms                                                                 | 114 ms: 1.01x faster                                                      |
| scimark_fft              | 344 ms                                                                 | 342 ms: 1.00x faster                                                      |
| python_startup           | 11.1 ms                                                                | 11.1 ms: 1.00x faster                                                     |
| python_startup_no_site   | 9.53 ms                                                                | 9.54 ms: 1.00x slower                                                     |
| generators               | 29.7 ms                                                                | 29.9 ms: 1.01x slower                                                     |
| 2to3                     | 278 ms                                                                 | 280 ms: 1.01x slower                                                      |
| sqlite_synth             | 2.86 us                                                                | 2.88 us: 1.01x slower                                                     |
| regex_v8                 | 25.5 ms                                                                | 25.7 ms: 1.01x slower                                                     |
| json_dumps               | 10.6 ms                                                                | 10.7 ms: 1.01x slower                                                     |
| sympy_sum                | 166 ms                                                                 | 167 ms: 1.01x slower                                                      |
| meteor_contest           | 110 ms                                                                 | 111 ms: 1.01x slower                                                      |
| regex_effbot             | 3.74 ms                                                                | 3.78 ms: 1.01x slower                                                     |
| docutils                 | 2.89 sec                                                               | 2.93 sec: 1.01x slower                                                    |
| mako                     | 10.7 ms                                                                | 10.8 ms: 1.01x slower                                                     |
| crypto_pyaes             | 74.6 ms                                                                | 75.6 ms: 1.01x slower                                                     |
| sqlglot_normalize        | 113 ms                                                                 | 114 ms: 1.01x slower                                                      |
| coverage                 | 96.3 ms                                                                | 97.8 ms: 1.02x slower                                                     |
| pycparser                | 1.23 sec                                                               | 1.25 sec: 1.02x slower                                                    |
| dulwich_log              | 70.6 ms                                                                | 71.8 ms: 1.02x slower                                                     |
| sympy_expand             | 491 ms                                                                 | 500 ms: 1.02x slower                                                      |
| create_gc_cycles         | 1.66 ms                                                                | 1.69 ms: 1.02x slower                                                     |
| thrift                   | 806 us                                                                 | 822 us: 1.02x slower                                                      |
| genshi_text              | 25.3 ms                                                                | 25.8 ms: 1.02x slower                                                     |
| json                     | 5.36 ms                                                                | 5.47 ms: 1.02x slower                                                     |
| xml_etree_process        | 61.3 ms                                                                | 62.6 ms: 1.02x slower                                                     |
| pathlib                  | 19.0 ms                                                                | 19.4 ms: 1.02x slower                                                     |
| sympy_str                | 289 ms                                                                 | 296 ms: 1.02x slower                                                      |
| logging_simple           | 5.92 us                                                                | 6.07 us: 1.02x slower                                                     |
| sympy_integrate          | 21.8 ms                                                                | 22.4 ms: 1.03x slower                                                     |
| gc_traversal             | 3.69 ms                                                                | 3.78 ms: 1.03x slower                                                     |
| django_template          | 36.2 ms                                                                | 37.1 ms: 1.03x slower                                                     |
| sqlglot_parse            | 1.34 ms                                                                | 1.37 ms: 1.03x slower                                                     |
| logging_format           | 6.54 us                                                                | 6.71 us: 1.03x slower                                                     |
| pickle_list              | 4.99 us                                                                | 5.12 us: 1.03x slower                                                     |
| pickle                   | 11.8 us                                                                | 12.1 us: 1.03x slower                                                     |
| deepcopy                 | 359 us                                                                 | 370 us: 1.03x slower                                                      |
| raytrace                 | 294 ms                                                                 | 303 ms: 1.03x slower                                                      |
| chaos                    | 63.4 ms                                                                | 65.4 ms: 1.03x slower                                                     |
| telco                    | 8.58 ms                                                                | 8.85 ms: 1.03x slower                                                     |
| sqlglot_optimize         | 57.6 ms                                                                | 59.5 ms: 1.03x slower                                                     |
| sqlglot_transpile        | 1.65 ms                                                                | 1.71 ms: 1.03x slower                                                     |
| deepcopy_reduce          | 3.17 us                                                                | 3.27 us: 1.03x slower                                                     |
| regex_compile            | 146 ms                                                                 | 151 ms: 1.03x slower                                                      |
| pprint_safe_repr         | 741 ms                                                                 | 767 ms: 1.04x slower                                                      |
| mdp                      | 2.65 sec                                                               | 2.75 sec: 1.04x slower                                                    |
| bench_thread_pool        | 858 us                                                                 | 890 us: 1.04x slower                                                      |
| tomli_loads              | 2.06 sec                                                               | 2.13 sec: 1.04x slower                                                    |
| chameleon                | 6.89 ms                                                                | 7.16 ms: 1.04x slower                                                     |
| float                    | 76.5 ms                                                                | 79.6 ms: 1.04x slower                                                     |
| logging_silent           | 102 ns                                                                 | 106 ns: 1.04x slower                                                      |
| typing_runtime_protocols | 111 us                                                                 | 116 us: 1.04x slower                                                      |
| xml_etree_iterparse      | 107 ms                                                                 | 112 ms: 1.05x slower                                                      |
| regex_dna                | 224 ms                                                                 | 234 ms: 1.05x slower                                                      |
| xml_etree_generate       | 88.6 ms                                                                | 92.9 ms: 1.05x slower                                                     |
| genshi_xml               | 54.6 ms                                                                | 57.3 ms: 1.05x slower                                                     |
| pprint_pformat           | 1.52 sec                                                               | 1.60 sec: 1.05x slower                                                    |
| fannkuch                 | 388 ms                                                                 | 410 ms: 1.06x slower                                                      |
| comprehensions           | 18.3 us                                                                | 19.4 us: 1.06x slower                                                     |
| scimark_monte_carlo      | 70.7 ms                                                                | 75.3 ms: 1.07x slower                                                     |
| pickle_dict              | 34.2 us                                                                | 36.5 us: 1.07x slower                                                     |
| async_generators         | 457 ms                                                                 | 502 ms: 1.10x slower                                                      |
| unpickle_pure_python     | 240 us                                                                 | 268 us: 1.12x slower                                                      |
| go                       | 156 ms                                                                 | 175 ms: 1.12x slower                                                      |
| richards_super           | 52.6 ms                                                                | 59.7 ms: 1.13x slower                                                     |
| hexiom                   | 7.12 ms                                                                | 8.12 ms: 1.14x slower                                                     |
| unpickle                 | 15.0 us                                                                | 17.1 us: 1.14x slower                                                     |
| deepcopy_memo            | 38.9 us                                                                | 44.8 us: 1.15x slower                                                     |
| richards                 | 46.7 ms                                                                | 54.0 ms: 1.16x slower                                                     |
| deltablue                | 3.50 ms                                                                | 4.15 ms: 1.19x slower                                                     |
| nqueens                  | 91.9 ms                                                                | 109 ms: 1.19x slower                                                      |
| Geometric mean           | (ref)                                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (26): async_tree_io, djangocms, aiohttp, async_tree_memoization, async_tree_memoization_tg, gunicorn, unpickle_list, scimark_sor, bench_mp_pool, json_loads, asyncio_websockets, asyncio_tcp, asyncio_tcp_ssl, pidigits, tornado_http, pyflate, coroutines, nbody, xml_etree_parse, pickle_pure_python, dask, async_tree_cpu_io_mixed_tg, pylint, async_tree_cpu_io_mixed, async_tree_none_tg, mypy2


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.01x