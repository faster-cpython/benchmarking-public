
# Results vs. 3.10.4

- fork: python
- ref: d3b9134ebb40bdb01ff5
- machine: linux-x86_64
- commit hash: d3b9134
- commit date: 2021-05-03
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 333 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 141 ms: 1.02x faster                                                   |
| float          | 109 ms                                                 | 107 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 171 ms: 1.04x faster                                                   |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                                   |
| regex_v8       | 25.0 ms                                                | 25.4 ms: 1.01x slower                                                  |
| regex_effbot   | 3.19 ms                                                | 3.24 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_list          | 4.72 us                                                | 4.45 us: 1.06x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 294 us: 1.03x faster                                                   |
| pickle_dict          | 27.6 us                                                | 26.9 us: 1.02x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 73.2 ms: 1.02x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 92.4 ms: 1.02x faster                                                  |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                                  |
| json_loads           | 28.7 us                                                | 28.4 us: 1.01x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 110 ms: 1.01x faster                                                   |
| json_dumps           | 13.4 ms                                                | 13.7 ms: 1.02x slower                                                  |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 5.78 ms                                                | 5.79 ms: 1.00x slower                                                  |
| python_startup         | 14.1 ms                                                | 15.2 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 30.6 ms                                                | 30.1 ms: 1.02x faster                                                  |
| genshi_xml     | 63.7 ms                                                | 63.2 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 61.6 ms: 1.24x faster                                                  |
| coverage                | 74.7 ms                                                | 65.8 ms: 1.14x faster                                                  |
| pickle_list             | 4.72 us                                                | 4.45 us: 1.06x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 48.8 us: 1.06x faster                                                  |
| pathlib                 | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                  |
| logging_silent          | 176 ns                                                 | 169 ns: 1.04x faster                                                   |
| fannkuch                | 488 ms                                                 | 467 ms: 1.04x faster                                                   |
| pylint                  | 532 ms                                                 | 512 ms: 1.04x faster                                                   |
| coroutines              | 31.6 ms                                                | 30.4 ms: 1.04x faster                                                  |
| regex_compile           | 177 ms                                                 | 171 ms: 1.04x faster                                                   |
| richards                | 75.2 ms                                                | 72.6 ms: 1.04x faster                                                  |
| deepcopy                | 438 us                                                 | 423 us: 1.03x faster                                                   |
| nqueens                 | 100 ms                                                 | 97.2 ms: 1.03x faster                                                  |
| meteor_contest          | 114 ms                                                 | 111 ms: 1.03x faster                                                   |
| unpickle_pure_python    | 302 us                                                 | 294 us: 1.03x faster                                                   |
| scimark_fft             | 421 ms                                                 | 411 ms: 1.02x faster                                                   |
| asyncio_tcp             | 914 ms                                                 | 893 ms: 1.02x faster                                                   |
| thrift                  | 1.03 ms                                                | 1.01 ms: 1.02x faster                                                  |
| pickle_dict             | 27.6 us                                                | 26.9 us: 1.02x faster                                                  |
| pyflate                 | 676 ms                                                 | 660 ms: 1.02x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 106 ms: 1.02x faster                                                   |
| pprint_pformat          | 1.98 sec                                               | 1.94 sec: 1.02x faster                                                 |
| nbody                   | 144 ms                                                 | 141 ms: 1.02x faster                                                   |
| hexiom                  | 9.43 ms                                                | 9.25 ms: 1.02x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 73.2 ms: 1.02x faster                                                  |
| float                   | 109 ms                                                 | 107 ms: 1.02x faster                                                   |
| json                    | 5.35 ms                                                | 5.26 ms: 1.02x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 938 ms: 1.02x faster                                                   |
| genshi_text             | 30.6 ms                                                | 30.1 ms: 1.02x faster                                                  |
| deepcopy_reduce         | 3.79 us                                                | 3.73 us: 1.02x faster                                                  |
| async_generators        | 426 ms                                                 | 420 ms: 1.02x faster                                                   |
| xml_etree_generate      | 93.8 ms                                                | 92.4 ms: 1.02x faster                                                  |
| logging_format          | 8.85 us                                                | 8.72 us: 1.02x faster                                                  |
| gc_traversal            | 3.53 ms                                                | 3.48 ms: 1.01x faster                                                  |
| logging_simple          | 8.10 us                                                | 8.01 us: 1.01x faster                                                  |
| scimark_sor             | 197 ms                                                 | 195 ms: 1.01x faster                                                   |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                                  |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                                   |
| json_loads              | 28.7 us                                                | 28.4 us: 1.01x faster                                                  |
| sympy_str               | 325 ms                                                 | 322 ms: 1.01x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 110 ms: 1.01x faster                                                   |
| async_tree_memoization  | 855 ms                                                 | 848 ms: 1.01x faster                                                   |
| go                      | 226 ms                                                 | 224 ms: 1.01x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 63.2 ms: 1.01x faster                                                  |
| sympy_integrate         | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                  |
| 2to3                    | 335 ms                                                 | 333 ms: 1.01x faster                                                   |
| sympy_expand            | 534 ms                                                 | 531 ms: 1.00x faster                                                   |
| python_startup_no_site  | 5.78 ms                                                | 5.79 ms: 1.00x slower                                                  |
| chaos                   | 106 ms                                                 | 106 ms: 1.00x slower                                                   |
| sqlglot_normalize       | 134 ms                                                 | 135 ms: 1.01x slower                                                   |
| crypto_pyaes            | 117 ms                                                 | 118 ms: 1.01x slower                                                   |
| async_tree_io           | 1.78 sec                                               | 1.80 sec: 1.01x slower                                                 |
| regex_v8                | 25.0 ms                                                | 25.4 ms: 1.01x slower                                                  |
| sqlglot_optimize        | 65.2 ms                                                | 66.1 ms: 1.01x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.24 ms: 1.01x slower                                                  |
| bench_thread_pool       | 946 us                                                 | 960 us: 1.01x slower                                                   |
| create_gc_cycles        | 1.65 ms                                                | 1.67 ms: 1.02x slower                                                  |
| json_dumps              | 13.4 ms                                                | 13.7 ms: 1.02x slower                                                  |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                                  |
| mdp                     | 2.74 sec                                               | 2.82 sec: 1.03x slower                                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 977 ms: 1.03x slower                                                   |
| python_startup          | 14.1 ms                                                | 15.2 ms: 1.08x slower                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 2.97 ms: 1.22x slower                                                  |
| sqlglot_parse           | 2.04 ms                                                | 2.57 ms: 1.26x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (22): djangocms, pycparser, unpack_sequence, scimark_lu, pickle_pure_python, dulwich_log, docutils, django_template, scimark_sparse_mat_mult, raytrace, spectral_norm, bench_mp_pool, sympy_sum, pidigits, mako, async_tree_none, deltablue, telco, sqlite_synth, html5lib, tornado_http, unpickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
