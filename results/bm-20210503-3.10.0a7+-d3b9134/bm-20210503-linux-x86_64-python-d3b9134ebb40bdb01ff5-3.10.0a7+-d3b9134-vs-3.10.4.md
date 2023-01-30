
# Results vs. 3.10.4

- fork: python
- ref: d3b9134ebb40bdb01ff5
- machine: linux-x86_64
- commit hash: d3b9134
- commit date: 2021-05-03
- overall geometric mean: 1.00x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 333 ms: 1.00x slower                                                   |
| docutils       | 3.18 sec                                               | 3.17 sec: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| nbody          | 136 ms                                                 | 141 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 171 ms: 1.02x faster                                                   |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                                   |
| regex_effbot   | 3.21 ms                                                | 3.24 ms: 1.01x slower                                                  |
| regex_v8       | 25.0 ms                                                | 25.4 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                   |
| pickle_dict          | 28.3 us                                                | 26.9 us: 1.05x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 73.2 ms: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                | 28.4 us: 1.02x faster                                                  |
| pickle_list          | 4.50 us                                                | 4.45 us: 1.01x faster                                                  |
| unpickle_pure_python | 297 us                                                 | 294 us: 1.01x faster                                                   |
| xml_etree_generate   | 93.3 ms                                                | 92.4 ms: 1.01x faster                                                  |
| unpickle             | 14.3 us                                                | 14.3 us: 1.00x slower                                                  |
| json_dumps           | 13.5 ms                                                | 13.7 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (4): pickle, pickle_pure_python, xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 5.76 ms                                                | 5.79 ms: 1.00x slower                                                  |
| python_startup         | 13.9 ms                                                | 15.2 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 30.6 ms                                                | 30.1 ms: 1.02x faster                                                  |
| mako           | 14.3 ms                                                | 14.7 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.8 ms                                                | 61.6 ms: 1.23x faster                                                  |
| coverage                | 75.3 ms                                                | 65.8 ms: 1.14x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                  |
| pickle_dict             | 28.3 us                                                | 26.9 us: 1.05x faster                                                  |
| coroutines              | 31.7 ms                                                | 30.4 ms: 1.04x faster                                                  |
| meteor_contest          | 114 ms                                                 | 111 ms: 1.03x faster                                                   |
| logging_silent          | 173 ns                                                 | 169 ns: 1.03x faster                                                   |
| deepcopy_memo           | 50.0 us                                                | 48.8 us: 1.02x faster                                                  |
| logging_format          | 8.92 us                                                | 8.72 us: 1.02x faster                                                  |
| pyflate                 | 675 ms                                                 | 660 ms: 1.02x faster                                                   |
| nqueens                 | 99.3 ms                                                | 97.2 ms: 1.02x faster                                                  |
| thrift                  | 1.03 ms                                                | 1.01 ms: 1.02x faster                                                  |
| fannkuch                | 477 ms                                                 | 467 ms: 1.02x faster                                                   |
| async_generators        | 428 ms                                                 | 420 ms: 1.02x faster                                                   |
| json                    | 5.35 ms                                                | 5.26 ms: 1.02x faster                                                  |
| hexiom                  | 9.42 ms                                                | 9.25 ms: 1.02x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 73.2 ms: 1.02x faster                                                  |
| regex_compile           | 174 ms                                                 | 171 ms: 1.02x faster                                                   |
| json_loads              | 28.9 us                                                | 28.4 us: 1.02x faster                                                  |
| pprint_pformat          | 1.97 sec                                               | 1.94 sec: 1.02x faster                                                 |
| genshi_text             | 30.6 ms                                                | 30.1 ms: 1.02x faster                                                  |
| deltablue               | 7.39 ms                                                | 7.29 ms: 1.01x faster                                                  |
| pylint                  | 519 ms                                                 | 512 ms: 1.01x faster                                                   |
| deepcopy                | 429 us                                                 | 423 us: 1.01x faster                                                   |
| go                      | 226 ms                                                 | 224 ms: 1.01x faster                                                   |
| pickle_list             | 4.50 us                                                | 4.45 us: 1.01x faster                                                  |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                                   |
| sympy_expand            | 537 ms                                                 | 531 ms: 1.01x faster                                                   |
| unpickle_pure_python    | 297 us                                                 | 294 us: 1.01x faster                                                   |
| xml_etree_generate      | 93.3 ms                                                | 92.4 ms: 1.01x faster                                                  |
| sympy_str               | 324 ms                                                 | 322 ms: 1.01x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 848 ms: 1.01x faster                                                   |
| scimark_fft             | 414 ms                                                 | 411 ms: 1.01x faster                                                   |
| float                   | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| deepcopy_reduce         | 3.75 us                                                | 3.73 us: 1.01x faster                                                  |
| logging_simple          | 8.06 us                                                | 8.01 us: 1.01x faster                                                  |
| pprint_safe_repr        | 943 ms                                                 | 938 ms: 1.01x faster                                                   |
| docutils                | 3.18 sec                                               | 3.17 sec: 1.00x faster                                                 |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| 2to3                    | 332 ms                                                 | 333 ms: 1.00x slower                                                   |
| python_startup_no_site  | 5.76 ms                                                | 5.79 ms: 1.00x slower                                                  |
| unpickle                | 14.3 us                                                | 14.3 us: 1.00x slower                                                  |
| scimark_sor             | 193 ms                                                 | 195 ms: 1.01x slower                                                   |
| spectral_norm           | 148 ms                                                 | 149 ms: 1.01x slower                                                   |
| raytrace                | 461 ms                                                 | 466 ms: 1.01x slower                                                   |
| regex_effbot            | 3.21 ms                                                | 3.24 ms: 1.01x slower                                                  |
| scimark_lu              | 158 ms                                                 | 160 ms: 1.01x slower                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 66.1 ms: 1.01x slower                                                  |
| sqlite_synth            | 2.90 us                                                | 2.94 us: 1.01x slower                                                  |
| async_tree_io           | 1.78 sec                                               | 1.80 sec: 1.01x slower                                                 |
| json_dumps              | 13.5 ms                                                | 13.7 ms: 1.01x slower                                                  |
| scimark_monte_carlo     | 105 ms                                                 | 106 ms: 1.01x slower                                                   |
| regex_v8                | 25.0 ms                                                | 25.4 ms: 1.02x slower                                                  |
| richards                | 71.4 ms                                                | 72.6 ms: 1.02x slower                                                  |
| bench_thread_pool       | 943 us                                                 | 960 us: 1.02x slower                                                   |
| chaos                   | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| mako                    | 14.3 ms                                                | 14.7 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 977 ms: 1.03x slower                                                   |
| nbody                   | 136 ms                                                 | 141 ms: 1.03x slower                                                   |
| python_startup          | 13.9 ms                                                | 15.2 ms: 1.09x slower                                                  |
| sqlglot_transpile       | 2.42 ms                                                | 2.97 ms: 1.23x slower                                                  |
| sqlglot_parse           | 2.04 ms                                                | 2.57 ms: 1.26x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (20): pickle, unpack_sequence, scimark_sparse_mat_mult, pickle_pure_python, genshi_xml, xml_etree_iterparse, async_tree_none, sympy_integrate, django_template, sympy_sum, mdp, bench_mp_pool, sqlglot_normalize, dulwich_log, crypto_pyaes, unpickle_list, pycparser, html5lib, tornado_http, telco
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20210503-3.10.0a7+-d3b9134/bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal
