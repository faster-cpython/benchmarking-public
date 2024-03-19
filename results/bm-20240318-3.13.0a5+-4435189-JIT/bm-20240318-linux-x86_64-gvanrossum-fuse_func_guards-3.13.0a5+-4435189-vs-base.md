# Results vs. base

- fork: gvanrossum
- ref: fuse_func_guards
- machine: linux-x86_64
- commit hash: 4435189
- commit date: 2024-03-18
- overall geometric mean: 1.00x faster
- HPT reliability: 51.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5+-4159644 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| html5lib       | 67.2 ms                                                                | 65.9 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (4): 2to3, chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5+-4159644 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io    | 1.22 sec                                                               | 1.21 sec: 1.01x faster                                                 |
| async_tree_io_tg | 1.22 sec                                                               | 1.23 sec: 1.01x slower                                                 |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (6): async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5+-4159644 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 92.2 ms                                                                | 93.2 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5+-4159644 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                 | 224 ms: 1.01x faster                                                   |
| regex_v8       | 25.5 ms                                                                | 25.7 ms: 1.01x slower                                                  |
| regex_effbot   | 3.73 ms                                                                | 3.78 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5+-4159644 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 319 us                                                                 | 306 us: 1.04x faster                                                   |
| unpickle_list        | 5.13 us                                                                | 5.07 us: 1.01x faster                                                  |
| unpickle_pure_python | 241 us                                                                 | 239 us: 1.01x faster                                                   |
| pickle_list          | 5.03 us                                                                | 5.01 us: 1.00x faster                                                  |
| xml_etree_process    | 60.7 ms                                                                | 60.4 ms: 1.00x faster                                                  |
| tomli_loads          | 2.07 sec                                                               | 2.09 sec: 1.01x slower                                                 |
| json_dumps           | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 108 ms                                                                 | 109 ms: 1.01x slower                                                   |
| unpickle             | 15.0 us                                                                | 15.5 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (5): json_loads, pickle_dict, xml_etree_parse, pickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5+-4159644 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 11.2 ms                                                                | 11.2 ms: 1.00x faster                                                  |
| python_startup         | 12.7 ms                                                                | 12.6 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5+-4159644 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 35.1 ms                                                                | 34.5 ms: 1.02x faster                                                  |
| genshi_xml      | 55.7 ms                                                                | 56.5 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5+-4159644 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpack_sequence          | 90.5 ns                                                                | 86.8 ns: 1.04x faster                                                  |
| pycparser                | 1.25 sec                                                               | 1.20 sec: 1.04x faster                                                 |
| pickle_pure_python       | 319 us                                                                 | 306 us: 1.04x faster                                                   |
| pyflate                  | 496 ms                                                                 | 481 ms: 1.03x faster                                                   |
| json                     | 5.27 ms                                                                | 5.12 ms: 1.03x faster                                                  |
| logging_silent           | 103 ns                                                                 | 100 ns: 1.02x faster                                                   |
| spectral_norm            | 117 ms                                                                 | 114 ms: 1.02x faster                                                   |
| djangocms                | 32.1 us                                                                | 31.4 us: 1.02x faster                                                  |
| deepcopy_memo            | 39.9 us                                                                | 39.0 us: 1.02x faster                                                  |
| html5lib                 | 67.2 ms                                                                | 65.9 ms: 1.02x faster                                                  |
| chaos                    | 65.4 ms                                                                | 64.2 ms: 1.02x faster                                                  |
| django_template          | 35.1 ms                                                                | 34.5 ms: 1.02x faster                                                  |
| richards_super           | 53.4 ms                                                                | 52.6 ms: 1.02x faster                                                  |
| richards                 | 47.2 ms                                                                | 46.5 ms: 1.01x faster                                                  |
| pprint_safe_repr         | 768 ms                                                                 | 758 ms: 1.01x faster                                                   |
| fannkuch                 | 402 ms                                                                 | 397 ms: 1.01x faster                                                   |
| deepcopy                 | 353 us                                                                 | 348 us: 1.01x faster                                                   |
| raytrace                 | 296 ms                                                                 | 293 ms: 1.01x faster                                                   |
| create_gc_cycles         | 1.53 ms                                                                | 1.51 ms: 1.01x faster                                                  |
| deepcopy_reduce          | 3.11 us                                                                | 3.08 us: 1.01x faster                                                  |
| typing_runtime_protocols | 113 us                                                                 | 112 us: 1.01x faster                                                   |
| unpickle_list            | 5.13 us                                                                | 5.07 us: 1.01x faster                                                  |
| unpickle_pure_python     | 241 us                                                                 | 239 us: 1.01x faster                                                   |
| thrift                   | 808 us                                                                 | 802 us: 1.01x faster                                                   |
| coroutines               | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                  |
| async_tree_io            | 1.22 sec                                                               | 1.21 sec: 1.01x faster                                                 |
| sqlglot_normalize        | 109 ms                                                                 | 108 ms: 1.01x faster                                                   |
| regex_dna                | 225 ms                                                                 | 224 ms: 1.01x faster                                                   |
| pickle_list              | 5.03 us                                                                | 5.01 us: 1.00x faster                                                  |
| xml_etree_process        | 60.7 ms                                                                | 60.4 ms: 1.00x faster                                                  |
| python_startup_no_site   | 11.2 ms                                                                | 11.2 ms: 1.00x faster                                                  |
| python_startup           | 12.7 ms                                                                | 12.6 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.84 sec                                                               | 1.85 sec: 1.00x slower                                                 |
| mdp                      | 2.64 sec                                                               | 2.65 sec: 1.00x slower                                                 |
| asyncio_tcp              | 501 ms                                                                 | 504 ms: 1.01x slower                                                   |
| regex_v8                 | 25.5 ms                                                                | 25.7 ms: 1.01x slower                                                  |
| generators               | 29.4 ms                                                                | 29.6 ms: 1.01x slower                                                  |
| tomli_loads              | 2.07 sec                                                               | 2.09 sec: 1.01x slower                                                 |
| json_dumps               | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                                  |
| crypto_pyaes             | 75.3 ms                                                                | 75.9 ms: 1.01x slower                                                  |
| scimark_fft              | 343 ms                                                                 | 346 ms: 1.01x slower                                                   |
| meteor_contest           | 110 ms                                                                 | 111 ms: 1.01x slower                                                   |
| xml_etree_iterparse      | 108 ms                                                                 | 109 ms: 1.01x slower                                                   |
| scimark_lu               | 131 ms                                                                 | 132 ms: 1.01x slower                                                   |
| nbody                    | 92.2 ms                                                                | 93.2 ms: 1.01x slower                                                  |
| async_tree_io_tg         | 1.22 sec                                                               | 1.23 sec: 1.01x slower                                                 |
| telco                    | 8.35 ms                                                                | 8.44 ms: 1.01x slower                                                  |
| regex_effbot             | 3.73 ms                                                                | 3.78 ms: 1.01x slower                                                  |
| pathlib                  | 18.9 ms                                                                | 19.1 ms: 1.01x slower                                                  |
| genshi_xml               | 55.7 ms                                                                | 56.5 ms: 1.01x slower                                                  |
| gc_traversal             | 3.82 ms                                                                | 3.92 ms: 1.03x slower                                                  |
| unpickle                 | 15.0 us                                                                | 15.5 us: 1.03x slower                                                  |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (50): sqlglot_transpile, logging_format, nqueens, aiohttp, pprint_pformat, async_generators, float, hexiom, async_tree_none, deltablue, json_loads, scimark_sparse_mat_mult, pylint, sqlglot_parse, 2to3, scimark_monte_carlo, comprehensions, pickle_dict, chameleon, mypy2, gunicorn, go, async_tree_none_tg, async_tree_memoization_tg, dask, sqlite_synth, pidigits, async_tree_memoization, sympy_integrate, docutils, asyncio_websockets, sqlglot_optimize, regex_compile, async_tree_cpu_io_mixed_tg, sympy_sum, bench_thread_pool, dulwich_log, sympy_str, coverage, bench_mp_pool, tornado_http, xml_etree_parse, pickle, sympy_expand, logging_simple, genshi_text, mako, xml_etree_generate, async_tree_cpu_io_mixed, scimark_sor


# HPT report

- Reliability score: 51.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.00x