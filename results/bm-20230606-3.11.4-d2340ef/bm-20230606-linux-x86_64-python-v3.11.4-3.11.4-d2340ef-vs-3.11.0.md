
# Results vs. 3.11.0

- fork: python
- ref: v3.11.4
- machine: linux-x86_64
- commit hash: d2340ef
- commit date: 2023-06-06
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 258 ms: 1.00x faster                                   |
| chameleon      | 6.47 ms                                                | 6.58 ms: 1.02x slower                                  |
| docutils       | 2.63 sec                                               | 2.57 sec: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| nbody          | 93.1 ms                                                | 99.4 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.45 ms: 1.16x faster                                  |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle             | 13.7 us                                                | 13.1 us: 1.05x faster                                  |
| pickle               | 10.1 us                                                | 9.76 us: 1.03x faster                                  |
| pickle_list          | 4.11 us                                                | 4.01 us: 1.03x faster                                  |
| tomli_loads          | 2.22 sec                                               | 2.19 sec: 1.01x faster                                 |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                  |
| pickle_pure_python   | 306 us                                                 | 302 us: 1.01x faster                                   |
| json_loads           | 26.5 us                                                | 26.2 us: 1.01x faster                                  |
| unpickle_pure_python | 228 us                                                 | 229 us: 1.00x slower                                   |
| xml_etree_generate   | 76.2 ms                                                | 76.5 ms: 1.00x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.02 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (4): xml_etree_process, json_dumps, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 6.01 ms: 1.00x faster                                  |
| python_startup         | 8.52 ms                                                | 8.53 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.80 ms: 1.03x faster                                  |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                  |
| genshi_text     | 21.6 ms                                                | 22.4 ms: 1.04x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot             | 3.99 ms                                                | 3.45 ms: 1.16x faster                                  |
| unpickle                 | 13.7 us                                                | 13.1 us: 1.05x faster                                  |
| pidigits                 | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| pickle                   | 10.1 us                                                | 9.76 us: 1.03x faster                                  |
| spectral_norm            | 100 ms                                                 | 97.1 ms: 1.03x faster                                  |
| mako                     | 10.1 ms                                                | 9.80 ms: 1.03x faster                                  |
| pickle_list              | 4.11 us                                                | 4.01 us: 1.03x faster                                  |
| docutils                 | 2.63 sec                                               | 2.57 sec: 1.02x faster                                 |
| sqlglot_parse            | 1.40 ms                                                | 1.37 ms: 1.02x faster                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.67 ms: 1.02x faster                                  |
| async_generators         | 368 ms                                                 | 361 ms: 1.02x faster                                   |
| regex_dna                | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                  |
| logging_format           | 6.68 us                                                | 6.58 us: 1.02x faster                                  |
| deepcopy_memo            | 37.0 us                                                | 36.5 us: 1.02x faster                                  |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                   |
| pathlib                  | 18.2 ms                                                | 18.0 ms: 1.01x faster                                  |
| tomli_loads              | 2.22 sec                                               | 2.19 sec: 1.01x faster                                 |
| pickle_dict              | 31.1 us                                                | 30.7 us: 1.01x faster                                  |
| pickle_pure_python       | 306 us                                                 | 302 us: 1.01x faster                                   |
| json_loads               | 26.5 us                                                | 26.2 us: 1.01x faster                                  |
| sympy_expand             | 475 ms                                                 | 470 ms: 1.01x faster                                   |
| raytrace                 | 297 ms                                                 | 294 ms: 1.01x faster                                   |
| scimark_fft              | 328 ms                                                 | 326 ms: 1.01x faster                                   |
| gunicorn                 | 1.18 ms                                                | 1.17 ms: 1.01x faster                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 67.7 ms: 1.01x faster                                  |
| mdp                      | 2.62 sec                                               | 2.60 sec: 1.01x faster                                 |
| aiohttp                  | 1.10 ms                                                | 1.09 ms: 1.01x faster                                  |
| pprint_pformat           | 1.46 sec                                               | 1.45 sec: 1.00x faster                                 |
| sympy_integrate          | 21.0 ms                                                | 20.9 ms: 1.00x faster                                  |
| 2to3                     | 259 ms                                                 | 258 ms: 1.00x faster                                   |
| bench_thread_pool        | 819 us                                                 | 816 us: 1.00x faster                                   |
| sympy_sum                | 167 ms                                                 | 166 ms: 1.00x faster                                   |
| sqlglot_optimize         | 53.1 ms                                                | 53.0 ms: 1.00x faster                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.01 ms: 1.00x faster                                  |
| python_startup           | 8.52 ms                                                | 8.53 ms: 1.00x slower                                  |
| generators               | 73.5 ms                                                | 73.7 ms: 1.00x slower                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 3.15 sec: 1.00x slower                                 |
| unpickle_pure_python     | 228 us                                                 | 229 us: 1.00x slower                                   |
| xml_etree_generate       | 76.2 ms                                                | 76.5 ms: 1.00x slower                                  |
| comprehensions           | 22.4 us                                                | 22.6 us: 1.01x slower                                  |
| sqlglot_normalize        | 108 ms                                                 | 108 ms: 1.01x slower                                   |
| gc_traversal             | 4.02 ms                                                | 4.04 ms: 1.01x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 707 ms: 1.01x slower                                   |
| pyflate                  | 418 ms                                                 | 421 ms: 1.01x slower                                   |
| flaskblogging            | 7.12 ms                                                | 7.17 ms: 1.01x slower                                  |
| regex_v8                 | 22.0 ms                                                | 22.2 ms: 1.01x slower                                  |
| logging_simple           | 6.03 us                                                | 6.09 us: 1.01x slower                                  |
| deltablue                | 3.67 ms                                                | 3.71 ms: 1.01x slower                                  |
| django_template          | 32.6 ms                                                | 33.0 ms: 1.01x slower                                  |
| coroutines               | 25.5 ms                                                | 25.9 ms: 1.01x slower                                  |
| chaos                    | 69.2 ms                                                | 70.2 ms: 1.02x slower                                  |
| chameleon                | 6.47 ms                                                | 6.58 ms: 1.02x slower                                  |
| fannkuch                 | 388 ms                                                 | 394 ms: 1.02x slower                                   |
| async_tree_memoization   | 627 ms                                                 | 638 ms: 1.02x slower                                   |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                   |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.58 ms: 1.02x slower                                  |
| typing_runtime_protocols | 486 us                                                 | 495 us: 1.02x slower                                   |
| thrift                   | 756 us                                                 | 771 us: 1.02x slower                                   |
| hexiom                   | 6.37 ms                                                | 6.50 ms: 1.02x slower                                  |
| unpickle_list            | 4.91 us                                                | 5.02 us: 1.02x slower                                  |
| dulwich_log              | 63.7 ms                                                | 65.5 ms: 1.03x slower                                  |
| genshi_text              | 21.6 ms                                                | 22.4 ms: 1.04x slower                                  |
| richards_super           | 56.8 ms                                                | 60.0 ms: 1.06x slower                                  |
| richards                 | 45.7 ms                                                | 48.5 ms: 1.06x slower                                  |
| nbody                    | 93.1 ms                                                | 99.4 ms: 1.07x slower                                  |
| mypy2                    | 420 ms                                                 | 534 ms: 1.27x slower                                   |
| Geometric mean           | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (32): meteor_contest, pylint, sqlite_synth, async_tree_none, html5lib, scimark_lu, scimark_sor, nqueens, float, sqlalchemy_imperative, deepcopy, crypto_pyaes, async_tree_io, async_tree_cpu_io_mixed, sympy_str, create_gc_cycles, bench_mp_pool, go, asyncio_tcp, deepcopy_reduce, dask, pycparser, xml_etree_process, genshi_xml, json_dumps, sqlalchemy_declarative, tornado_http, xml_etree_iterparse, telco, xml_etree_parse, unpack_sequence, djangocms
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: coverage
