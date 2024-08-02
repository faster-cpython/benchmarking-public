# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: deferred_rc_overhead
- machine: linux-x86_64
- commit hash: e12729e
- commit date: 2024-05-30
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.81 sec: 1.01x faster                                                          |
| html5lib       | 67.2 ms                                                    | 66.7 ms: 1.01x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|--------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 389 ms: 1.03x slower                                                            |
| async_tree_io_tg   | 936 ms                                                     | 973 ms: 1.04x slower                                                            |
| async_tree_none_tg | 336 ms                                                     | 356 ms: 1.06x slower                                                            |
| Geometric mean     | (ref)                                                      | 1.03x slower                                                                    |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| float          | 78.9 ms                                                    | 79.6 ms: 1.01x slower                                                           |
| nbody          | 88.3 ms                                                    | 92.4 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                           |
| regex_compile  | 137 ms                                                     | 137 ms: 1.00x slower                                                            |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.80 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| pickle_list          | 5.11 us                                                    | 5.14 us: 1.01x slower                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 88.3 ms: 1.01x slower                                                           |
| unpickle             | 15.1 us                                                    | 15.3 us: 1.01x slower                                                           |
| pickle_dict          | 34.8 us                                                    | 35.3 us: 1.01x slower                                                           |
| unpickle_list        | 5.34 us                                                    | 5.43 us: 1.02x slower                                                           |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| pickle_pure_python   | 305 us                                                     | 313 us: 1.03x slower                                                            |
| unpickle_pure_python | 218 us                                                     | 225 us: 1.03x slower                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.22 sec: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                           |
| genshi_text     | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 52.6 ms: 1.02x slower                                                           |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                      | 2.79 sec                                                   | 2.59 sec: 1.08x faster                                                          |
| pathlib                  | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                           |
| gc_traversal             | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                           |
| richards                 | 50.9 ms                                                    | 49.8 ms: 1.02x faster                                                           |
| scimark_fft              | 392 ms                                                     | 384 ms: 1.02x faster                                                            |
| richards_super           | 57.4 ms                                                    | 56.2 ms: 1.02x faster                                                           |
| regex_v8                 | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                           |
| python_startup           | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| logging_silent           | 105 ns                                                     | 103 ns: 1.02x faster                                                            |
| scimark_lu               | 122 ms                                                     | 120 ms: 1.01x faster                                                            |
| create_gc_cycles         | 1.82 ms                                                    | 1.79 ms: 1.01x faster                                                           |
| json_dumps               | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| thrift                   | 823 us                                                     | 815 us: 1.01x faster                                                            |
| dulwich_log              | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                                           |
| html5lib                 | 67.2 ms                                                    | 66.7 ms: 1.01x faster                                                           |
| json                     | 5.31 ms                                                    | 5.28 ms: 1.01x faster                                                           |
| docutils                 | 2.83 sec                                                   | 2.81 sec: 1.01x faster                                                          |
| tornado_http             | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                                           |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 5.25 ms: 1.00x faster                                                           |
| python_startup_no_site   | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                           |
| bench_thread_pool        | 834 us                                                     | 836 us: 1.00x slower                                                            |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.85 sec: 1.00x slower                                                          |
| regex_compile            | 137 ms                                                     | 137 ms: 1.00x slower                                                            |
| crypto_pyaes             | 77.5 ms                                                    | 78.0 ms: 1.01x slower                                                           |
| sympy_sum                | 156 ms                                                     | 157 ms: 1.01x slower                                                            |
| pickle_list              | 5.11 us                                                    | 5.14 us: 1.01x slower                                                           |
| generators               | 29.6 ms                                                    | 29.9 ms: 1.01x slower                                                           |
| pyflate                  | 484 ms                                                     | 488 ms: 1.01x slower                                                            |
| sympy_integrate          | 20.5 ms                                                    | 20.7 ms: 1.01x slower                                                           |
| logging_simple           | 5.74 us                                                    | 5.80 us: 1.01x slower                                                           |
| fannkuch                 | 402 ms                                                     | 406 ms: 1.01x slower                                                            |
| float                    | 78.9 ms                                                    | 79.6 ms: 1.01x slower                                                           |
| sympy_expand             | 473 ms                                                     | 477 ms: 1.01x slower                                                            |
| xml_etree_generate       | 87.4 ms                                                    | 88.3 ms: 1.01x slower                                                           |
| mako                     | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                           |
| sqlglot_transpile        | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                           |
| unpickle                 | 15.1 us                                                    | 15.3 us: 1.01x slower                                                           |
| pprint_pformat           | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                                          |
| genshi_text              | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| spectral_norm            | 116 ms                                                     | 118 ms: 1.01x slower                                                            |
| sqlglot_optimize         | 55.5 ms                                                    | 56.3 ms: 1.01x slower                                                           |
| pickle_dict              | 34.8 us                                                    | 35.3 us: 1.01x slower                                                           |
| sqlglot_normalize        | 110 ms                                                     | 112 ms: 1.02x slower                                                            |
| unpickle_list            | 5.34 us                                                    | 5.43 us: 1.02x slower                                                           |
| deepcopy                 | 367 us                                                     | 374 us: 1.02x slower                                                            |
| go                       | 145 ms                                                     | 147 ms: 1.02x slower                                                            |
| pickle                   | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| genshi_xml               | 51.6 ms                                                    | 52.6 ms: 1.02x slower                                                           |
| meteor_contest           | 110 ms                                                     | 112 ms: 1.02x slower                                                            |
| regex_dna                | 221 ms                                                     | 226 ms: 1.02x slower                                                            |
| chaos                    | 61.3 ms                                                    | 62.6 ms: 1.02x slower                                                           |
| hexiom                   | 6.30 ms                                                    | 6.43 ms: 1.02x slower                                                           |
| pprint_safe_repr         | 758 ms                                                     | 774 ms: 1.02x slower                                                            |
| nqueens                  | 81.4 ms                                                    | 83.2 ms: 1.02x slower                                                           |
| coroutines               | 23.2 ms                                                    | 23.7 ms: 1.02x slower                                                           |
| telco                    | 8.41 ms                                                    | 8.60 ms: 1.02x slower                                                           |
| sqlglot_parse            | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                           |
| async_generators         | 442 ms                                                     | 452 ms: 1.02x slower                                                            |
| deltablue                | 3.25 ms                                                    | 3.33 ms: 1.02x slower                                                           |
| comprehensions           | 16.6 us                                                    | 17.0 us: 1.02x slower                                                           |
| pickle_pure_python       | 305 us                                                     | 313 us: 1.03x slower                                                            |
| async_tree_none          | 378 ms                                                     | 389 ms: 1.03x slower                                                            |
| raytrace                 | 267 ms                                                     | 274 ms: 1.03x slower                                                            |
| django_template          | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                           |
| unpickle_pure_python     | 218 us                                                     | 225 us: 1.03x slower                                                            |
| regex_effbot             | 3.67 ms                                                    | 3.80 ms: 1.04x slower                                                           |
| scimark_monte_carlo      | 69.2 ms                                                    | 71.9 ms: 1.04x slower                                                           |
| async_tree_io_tg         | 936 ms                                                     | 973 ms: 1.04x slower                                                            |
| typing_runtime_protocols | 165 us                                                     | 172 us: 1.04x slower                                                            |
| deepcopy_memo            | 39.7 us                                                    | 41.5 us: 1.04x slower                                                           |
| nbody                    | 88.3 ms                                                    | 92.4 ms: 1.05x slower                                                           |
| tomli_loads              | 2.12 sec                                                   | 2.22 sec: 1.05x slower                                                          |
| async_tree_none_tg       | 336 ms                                                     | 356 ms: 1.06x slower                                                            |
| Geometric mean           | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (22): xml_etree_parse, sqlite_synth, asyncio_websockets, 2to3, logging_format, bench_mp_pool, asyncio_tcp, dask, xml_etree_process, deepcopy_reduce, json_loads, pycparser, scimark_sor, xml_etree_iterparse, coverage, sympy_str, pylint, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x