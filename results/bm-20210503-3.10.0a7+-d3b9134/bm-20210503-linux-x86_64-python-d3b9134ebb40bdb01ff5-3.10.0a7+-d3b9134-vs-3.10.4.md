
# Results vs. 3.10.4

- fork: python
- ref: d3b9134ebb40bdb01ff5
- machine: linux-x86_64
- commit hash: d3b9134
- commit date: 2021-05-03
- overall geometric mean: 1.01x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 333 ms: 1.01x faster                                                   |
| tornado_http   | 127 ms                                                 | 129 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 107 ms: 1.03x faster                                                   |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                   |
| regex_compile  | 177 ms                                                 | 171 ms: 1.03x faster                                                   |
| regex_v8       | 25.0 ms                                                | 25.4 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                   |
| pickle               | 10.3 us                                                | 10.0 us: 1.03x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.45 us: 1.02x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 73.2 ms: 1.02x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 294 us: 1.02x faster                                                   |
| xml_etree_generate   | 94.2 ms                                                | 92.4 ms: 1.02x faster                                                  |
| json_loads           | 28.8 us                                                | 28.4 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 110 ms: 1.01x faster                                                   |
| pickle_dict          | 27.3 us                                                | 26.9 us: 1.01x faster                                                  |
| pickle_pure_python   | 455 us                                                 | 451 us: 1.01x faster                                                   |
| json_dumps           | 13.5 ms                                                | 13.7 ms: 1.01x slower                                                  |
| unpickle             | 14.1 us                                                | 14.3 us: 1.01x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 5.82 ms                                                | 5.79 ms: 1.00x faster                                                  |
| python_startup         | 14.2 ms                                                | 15.2 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 30.3 ms                                                | 30.1 ms: 1.01x faster                                                  |
| mako            | 14.8 ms                                                | 14.7 ms: 1.01x faster                                                  |
| django_template | 45.9 ms                                                | 46.2 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 61.6 ms: 1.25x faster                                                  |
| coverage                | 72.8 ms                                                | 65.8 ms: 1.11x faster                                                  |
| gc_traversal            | 3.84 ms                                                | 3.48 ms: 1.11x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 59.0 ns: 1.10x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 48.8 us: 1.07x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                  |
| regex_dna               | 222 ms                                                 | 211 ms: 1.05x faster                                                   |
| coroutines              | 31.8 ms                                                | 30.4 ms: 1.05x faster                                                  |
| deepcopy                | 442 us                                                 | 423 us: 1.04x faster                                                   |
| fannkuch                | 486 ms                                                 | 467 ms: 1.04x faster                                                   |
| logging_silent          | 175 ns                                                 | 169 ns: 1.04x faster                                                   |
| asyncio_tcp             | 925 ms                                                 | 893 ms: 1.04x faster                                                   |
| meteor_contest          | 115 ms                                                 | 111 ms: 1.04x faster                                                   |
| regex_compile           | 177 ms                                                 | 171 ms: 1.03x faster                                                   |
| float                   | 111 ms                                                 | 107 ms: 1.03x faster                                                   |
| richards                | 74.9 ms                                                | 72.6 ms: 1.03x faster                                                  |
| scimark_fft             | 424 ms                                                 | 411 ms: 1.03x faster                                                   |
| json                    | 5.42 ms                                                | 5.26 ms: 1.03x faster                                                  |
| nqueens                 | 100 ms                                                 | 97.2 ms: 1.03x faster                                                  |
| hexiom                  | 9.53 ms                                                | 9.25 ms: 1.03x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 3.73 us: 1.03x faster                                                  |
| sympy_expand            | 545 ms                                                 | 531 ms: 1.03x faster                                                   |
| pylint                  | 525 ms                                                 | 512 ms: 1.03x faster                                                   |
| pickle                  | 10.3 us                                                | 10.0 us: 1.03x faster                                                  |
| go                      | 229 ms                                                 | 224 ms: 1.02x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.45 us: 1.02x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 73.2 ms: 1.02x faster                                                  |
| thrift                  | 1.03 ms                                                | 1.01 ms: 1.02x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.94 sec: 1.02x faster                                                 |
| unpickle_pure_python    | 300 us                                                 | 294 us: 1.02x faster                                                   |
| logging_format          | 8.91 us                                                | 8.72 us: 1.02x faster                                                  |
| sympy_str               | 328 ms                                                 | 322 ms: 1.02x faster                                                   |
| xml_etree_generate      | 94.2 ms                                                | 92.4 ms: 1.02x faster                                                  |
| scimark_lu              | 163 ms                                                 | 160 ms: 1.02x faster                                                   |
| pyflate                 | 673 ms                                                 | 660 ms: 1.02x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 938 ms: 1.02x faster                                                   |
| deltablue               | 7.42 ms                                                | 7.29 ms: 1.02x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 23.9 ms: 1.02x faster                                                  |
| json_loads              | 28.8 us                                                | 28.4 us: 1.02x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 110 ms: 1.01x faster                                                   |
| async_generators        | 425 ms                                                 | 420 ms: 1.01x faster                                                   |
| pickle_dict             | 27.3 us                                                | 26.9 us: 1.01x faster                                                  |
| scimark_sor             | 197 ms                                                 | 195 ms: 1.01x faster                                                   |
| pickle_pure_python      | 455 us                                                 | 451 us: 1.01x faster                                                   |
| 2to3                    | 336 ms                                                 | 333 ms: 1.01x faster                                                   |
| logging_simple          | 8.07 us                                                | 8.01 us: 1.01x faster                                                  |
| sympy_sum               | 185 ms                                                 | 183 ms: 1.01x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 848 ms: 1.01x faster                                                   |
| genshi_text             | 30.3 ms                                                | 30.1 ms: 1.01x faster                                                  |
| mako                    | 14.8 ms                                                | 14.7 ms: 1.01x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 118 ms: 1.01x faster                                                   |
| python_startup_no_site  | 5.82 ms                                                | 5.79 ms: 1.00x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 75.6 ms: 1.00x faster                                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| raytrace                | 464 ms                                                 | 466 ms: 1.00x slower                                                   |
| django_template         | 45.9 ms                                                | 46.2 ms: 1.01x slower                                                  |
| json_dumps              | 13.5 ms                                                | 13.7 ms: 1.01x slower                                                  |
| pycparser               | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                 |
| sqlglot_optimize        | 65.3 ms                                                | 66.1 ms: 1.01x slower                                                  |
| regex_v8                | 25.0 ms                                                | 25.4 ms: 1.01x slower                                                  |
| bench_thread_pool       | 947 us                                                 | 960 us: 1.01x slower                                                   |
| unpickle                | 14.1 us                                                | 14.3 us: 1.01x slower                                                  |
| async_tree_io           | 1.77 sec                                               | 1.80 sec: 1.01x slower                                                 |
| tornado_http            | 127 ms                                                 | 129 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 977 ms: 1.03x slower                                                   |
| telco                   | 6.54 ms                                                | 6.74 ms: 1.03x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                                  |
| python_startup          | 14.2 ms                                                | 15.2 ms: 1.08x slower                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 2.97 ms: 1.21x slower                                                  |
| sqlglot_parse           | 2.06 ms                                                | 2.57 ms: 1.25x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (15): async_tree_none, nbody, spectral_norm, scimark_sparse_mat_mult, chaos, genshi_xml, sqlglot_normalize, docutils, mdp, bench_mp_pool, create_gc_cycles, sqlite_synth, regex_effbot, html5lib, djangocms
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, comprehensions, dask, flaskblogging, gunicorn, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
