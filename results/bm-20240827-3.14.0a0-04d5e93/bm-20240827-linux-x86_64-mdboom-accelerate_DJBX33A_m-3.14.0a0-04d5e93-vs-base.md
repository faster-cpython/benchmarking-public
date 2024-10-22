# Results vs. base

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-x86_64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.00x slower
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240826-linux-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                | 257 ms: 1.01x slower                                                  |
| docutils       | 2.70 sec                                                              | 2.72 sec: 1.01x slower                                                |
| html5lib       | 65.9 ms                                                               | 64.8 ms: 1.02x faster                                                 |
| tornado_http   | 90.3 ms                                                               | 90.5 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240826-linux-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines              | 23.4 ms                                                               | 22.9 ms: 1.02x faster                                                 |
| async_generators        | 438 ms                                                                | 433 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl         | 1.78 sec                                                              | 1.79 sec: 1.01x slower                                                |
| asyncio_tcp             | 477 ms                                                                | 482 ms: 1.01x slower                                                  |
| async_tree_io           | 916 ms                                                                | 929 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 553 ms                                                                | 561 ms: 1.02x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (7): async_tree_none_tg, asyncio_websockets, async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240826-linux-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 86.4 ms                                                               | 85.5 ms: 1.01x faster                                                 |
| float          | 77.6 ms                                                               | 77.1 ms: 1.01x faster                                                 |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240826-linux-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                | 220 ms: 1.01x faster                                                  |
| regex_effbot   | 3.74 ms                                                               | 3.73 ms: 1.00x faster                                                 |
| regex_v8       | 26.0 ms                                                               | 26.2 ms: 1.01x slower                                                 |
| regex_compile  | 128 ms                                                                | 131 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240826-linux-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.10 sec                                                              | 2.02 sec: 1.04x faster                                                |
| unpickle_pure_python | 215 us                                                                | 212 us: 1.01x faster                                                  |
| xml_etree_generate   | 84.8 ms                                                               | 85.0 ms: 1.00x slower                                                 |
| pickle_pure_python   | 300 us                                                                | 303 us: 1.01x slower                                                  |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240826-linux-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.04 ms: 1.01x faster                                                 |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240826-linux-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.4 ms                                                               | 11.3 ms: 1.01x faster                                                 |
| django_template | 33.9 ms                                                               | 34.3 ms: 1.01x slower                                                 |
| genshi_text     | 22.1 ms                                                               | 23.3 ms: 1.05x slower                                                 |
| genshi_xml      | 48.9 ms                                                               | 51.9 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240826-linux-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.99 ms                                                               | 4.68 ms: 1.07x faster                                                 |
| tomli_loads              | 2.10 sec                                                              | 2.02 sec: 1.04x faster                                                |
| deepcopy_memo            | 30.1 us                                                               | 29.3 us: 1.03x faster                                                 |
| scimark_fft              | 369 ms                                                                | 360 ms: 1.02x faster                                                  |
| coroutines               | 23.4 ms                                                               | 22.9 ms: 1.02x faster                                                 |
| spectral_norm            | 113 ms                                                                | 111 ms: 1.02x faster                                                  |
| richards_super           | 52.9 ms                                                               | 51.9 ms: 1.02x faster                                                 |
| html5lib                 | 65.9 ms                                                               | 64.8 ms: 1.02x faster                                                 |
| create_gc_cycles         | 1.76 ms                                                               | 1.73 ms: 1.02x faster                                                 |
| deltablue                | 3.23 ms                                                               | 3.19 ms: 1.02x faster                                                 |
| unpickle_pure_python     | 215 us                                                                | 212 us: 1.01x faster                                                  |
| regex_dna                | 223 ms                                                                | 220 ms: 1.01x faster                                                  |
| logging_simple           | 5.51 us                                                               | 5.44 us: 1.01x faster                                                 |
| async_generators         | 438 ms                                                                | 433 ms: 1.01x faster                                                  |
| nbody                    | 86.4 ms                                                               | 85.5 ms: 1.01x faster                                                 |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                                 |
| json                     | 5.26 ms                                                               | 5.21 ms: 1.01x faster                                                 |
| hexiom                   | 6.16 ms                                                               | 6.10 ms: 1.01x faster                                                 |
| go                       | 164 ms                                                                | 162 ms: 1.01x faster                                                  |
| richards                 | 46.8 ms                                                               | 46.4 ms: 1.01x faster                                                 |
| coverage                 | 85.5 ms                                                               | 84.9 ms: 1.01x faster                                                 |
| python_startup_no_site   | 7.09 ms                                                               | 7.04 ms: 1.01x faster                                                 |
| float                    | 77.6 ms                                                               | 77.1 ms: 1.01x faster                                                 |
| mako                     | 11.4 ms                                                               | 11.3 ms: 1.01x faster                                                 |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| regex_effbot             | 3.74 ms                                                               | 3.73 ms: 1.00x faster                                                 |
| xml_etree_generate       | 84.8 ms                                                               | 85.0 ms: 1.00x slower                                                 |
| gc_traversal             | 3.76 ms                                                               | 3.77 ms: 1.00x slower                                                 |
| mdp                      | 2.53 sec                                                              | 2.53 sec: 1.00x slower                                                |
| sympy_integrate          | 19.6 ms                                                               | 19.6 ms: 1.00x slower                                                 |
| tornado_http             | 90.3 ms                                                               | 90.5 ms: 1.00x slower                                                 |
| pidigits                 | 187 ms                                                                | 187 ms: 1.00x slower                                                  |
| pprint_pformat           | 1.47 sec                                                              | 1.48 sec: 1.00x slower                                                |
| 2to3                     | 255 ms                                                                | 257 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.79 sec: 1.01x slower                                                |
| docutils                 | 2.70 sec                                                              | 2.72 sec: 1.01x slower                                                |
| regex_v8                 | 26.0 ms                                                               | 26.2 ms: 1.01x slower                                                 |
| pathlib                  | 15.8 ms                                                               | 15.9 ms: 1.01x slower                                                 |
| generators               | 27.7 ms                                                               | 27.9 ms: 1.01x slower                                                 |
| pprint_safe_repr         | 719 ms                                                                | 724 ms: 1.01x slower                                                  |
| sympy_sum                | 147 ms                                                                | 148 ms: 1.01x slower                                                  |
| logging_silent           | 97.0 ns                                                               | 97.7 ns: 1.01x slower                                                 |
| raytrace                 | 259 ms                                                                | 261 ms: 1.01x slower                                                  |
| pickle_pure_python       | 300 us                                                                | 303 us: 1.01x slower                                                  |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                  |
| asyncio_tcp              | 477 ms                                                                | 482 ms: 1.01x slower                                                  |
| django_template          | 33.9 ms                                                               | 34.3 ms: 1.01x slower                                                 |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                 |
| deepcopy                 | 259 us                                                                | 262 us: 1.01x slower                                                  |
| async_tree_io            | 916 ms                                                                | 929 ms: 1.01x slower                                                  |
| pycparser                | 1.19 sec                                                              | 1.21 sec: 1.01x slower                                                |
| async_tree_cpu_io_mixed  | 553 ms                                                                | 561 ms: 1.02x slower                                                  |
| thrift                   | 760 us                                                                | 774 us: 1.02x slower                                                  |
| nqueens                  | 78.9 ms                                                               | 80.4 ms: 1.02x slower                                                 |
| regex_compile            | 128 ms                                                                | 131 ms: 1.02x slower                                                  |
| bpe_tokeniser            | 4.75 sec                                                              | 4.85 sec: 1.02x slower                                                |
| deepcopy_reduce          | 2.63 us                                                               | 2.69 us: 1.02x slower                                                 |
| pyflate                  | 452 ms                                                                | 466 ms: 1.03x slower                                                  |
| crypto_pyaes             | 71.6 ms                                                               | 74.0 ms: 1.03x slower                                                 |
| fannkuch                 | 393 ms                                                                | 406 ms: 1.03x slower                                                  |
| typing_runtime_protocols | 156 us                                                                | 163 us: 1.05x slower                                                  |
| genshi_text              | 22.1 ms                                                               | 23.3 ms: 1.05x slower                                                 |
| genshi_xml               | 48.9 ms                                                               | 51.9 ms: 1.06x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (26): json_loads, telco, async_tree_none_tg, sqlglot_parse, scimark_lu, asyncio_websockets, sympy_str, sqlglot_normalize, scimark_sor, bench_mp_pool, chaos, async_tree_none, bench_thread_pool, xml_etree_process, sqlglot_optimize, sqlglot_transpile, scimark_monte_carlo, xml_etree_parse, logging_format, async_tree_memoization_tg, sympy_expand, xml_etree_iterparse, pylint, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 99.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x