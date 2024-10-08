# Results vs. base

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-x86_64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.00x faster
- HPT reliability: 99.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                | 261 ms: 1.00x faster                                                            |
| html5lib       | 65.0 ms                                                               | 64.4 ms: 1.01x faster                                                           |
| tornado_http   | 90.1 ms                                                               | 89.5 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp_ssl | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                          |
| asyncio_tcp     | 488 ms                                                                | 491 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_generators, async_tree_memoization_tg, coroutines, async_tree_memoization, async_tree_none, async_tree_io, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                               | 25.4 ms: 1.03x faster                                                           |
| regex_effbot   | 3.72 ms                                                               | 3.64 ms: 1.02x faster                                                           |
| regex_compile  | 130 ms                                                                | 129 ms: 1.01x faster                                                            |
| regex_dna      | 219 ms                                                                | 220 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 27.9 us                                                               | 27.5 us: 1.01x faster                                                           |
| pickle_pure_python   | 298 us                                                                | 295 us: 1.01x faster                                                            |
| tomli_loads          | 2.05 sec                                                              | 2.04 sec: 1.01x faster                                                          |
| xml_etree_generate   | 84.3 ms                                                               | 84.6 ms: 1.00x slower                                                           |
| unpickle_pure_python | 209 us                                                                | 210 us: 1.00x slower                                                            |
| xml_etree_process    | 58.0 ms                                                               | 58.3 ms: 1.00x slower                                                           |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 7.11 ms                                                               | 7.07 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.9 ms                                                               | 10.7 ms: 1.02x faster                                                           |
| genshi_xml      | 49.3 ms                                                               | 48.6 ms: 1.01x faster                                                           |
| genshi_text     | 22.3 ms                                                               | 22.1 ms: 1.01x faster                                                           |
| django_template | 33.5 ms                                                               | 33.7 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                     | 2.70 sec                                                              | 2.57 sec: 1.05x faster                                                          |
| logging_silent          | 100 ns                                                                | 95.7 ns: 1.05x faster                                                           |
| logging_format          | 6.14 us                                                               | 5.96 us: 1.03x faster                                                           |
| crypto_pyaes            | 74.0 ms                                                               | 72.2 ms: 1.03x faster                                                           |
| regex_v8                | 26.1 ms                                                               | 25.4 ms: 1.03x faster                                                           |
| telco                   | 8.14 ms                                                               | 7.95 ms: 1.02x faster                                                           |
| regex_effbot            | 3.72 ms                                                               | 3.64 ms: 1.02x faster                                                           |
| deepcopy_memo           | 29.3 us                                                               | 28.6 us: 1.02x faster                                                           |
| hexiom                  | 6.10 ms                                                               | 5.98 ms: 1.02x faster                                                           |
| richards_super          | 52.1 ms                                                               | 51.2 ms: 1.02x faster                                                           |
| deltablue               | 3.16 ms                                                               | 3.11 ms: 1.02x faster                                                           |
| scimark_sor             | 122 ms                                                                | 121 ms: 1.02x faster                                                            |
| mako                    | 10.9 ms                                                               | 10.7 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult | 4.73 ms                                                               | 4.66 ms: 1.01x faster                                                           |
| json_loads              | 27.9 us                                                               | 27.5 us: 1.01x faster                                                           |
| genshi_xml              | 49.3 ms                                                               | 48.6 ms: 1.01x faster                                                           |
| thrift                  | 777 us                                                                | 768 us: 1.01x faster                                                            |
| pickle_pure_python      | 298 us                                                                | 295 us: 1.01x faster                                                            |
| pathlib                 | 15.8 ms                                                               | 15.6 ms: 1.01x faster                                                           |
| html5lib                | 65.0 ms                                                               | 64.4 ms: 1.01x faster                                                           |
| go                      | 141 ms                                                                | 140 ms: 1.01x faster                                                            |
| nqueens                 | 80.0 ms                                                               | 79.4 ms: 1.01x faster                                                           |
| sympy_sum               | 151 ms                                                                | 150 ms: 1.01x faster                                                            |
| sympy_str               | 271 ms                                                                | 269 ms: 1.01x faster                                                            |
| tornado_http            | 90.1 ms                                                               | 89.5 ms: 1.01x faster                                                           |
| comprehensions          | 16.6 us                                                               | 16.4 us: 1.01x faster                                                           |
| logging_simple          | 5.49 us                                                               | 5.46 us: 1.01x faster                                                           |
| genshi_text             | 22.3 ms                                                               | 22.1 ms: 1.01x faster                                                           |
| regex_compile           | 130 ms                                                                | 129 ms: 1.01x faster                                                            |
| tomli_loads             | 2.05 sec                                                              | 2.04 sec: 1.01x faster                                                          |
| python_startup          | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                           |
| meteor_contest          | 107 ms                                                                | 106 ms: 1.01x faster                                                            |
| pprint_pformat          | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                                          |
| python_startup_no_site  | 7.11 ms                                                               | 7.07 ms: 1.01x faster                                                           |
| sqlglot_transpile       | 1.57 ms                                                               | 1.57 ms: 1.00x faster                                                           |
| richards                | 46.0 ms                                                               | 45.8 ms: 1.00x faster                                                           |
| pprint_safe_repr        | 724 ms                                                                | 721 ms: 1.00x faster                                                            |
| sympy_integrate         | 19.7 ms                                                               | 19.6 ms: 1.00x faster                                                           |
| dulwich_log             | 63.8 ms                                                               | 63.5 ms: 1.00x faster                                                           |
| generators              | 28.0 ms                                                               | 27.9 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                          |
| bench_thread_pool       | 787 us                                                                | 784 us: 1.00x faster                                                            |
| spectral_norm           | 112 ms                                                                | 111 ms: 1.00x faster                                                            |
| 2to3                    | 261 ms                                                                | 261 ms: 1.00x faster                                                            |
| pidigits                | 187 ms                                                                | 187 ms: 1.00x faster                                                            |
| deepcopy                | 257 us                                                                | 258 us: 1.00x slower                                                            |
| xml_etree_generate      | 84.3 ms                                                               | 84.6 ms: 1.00x slower                                                           |
| unpickle_pure_python    | 209 us                                                                | 210 us: 1.00x slower                                                            |
| xml_etree_process       | 58.0 ms                                                               | 58.3 ms: 1.00x slower                                                           |
| django_template         | 33.5 ms                                                               | 33.7 ms: 1.01x slower                                                           |
| asyncio_tcp             | 488 ms                                                                | 491 ms: 1.01x slower                                                            |
| scimark_fft             | 357 ms                                                                | 359 ms: 1.01x slower                                                            |
| create_gc_cycles        | 1.73 ms                                                               | 1.74 ms: 1.01x slower                                                           |
| regex_dna               | 219 ms                                                                | 220 ms: 1.01x slower                                                            |
| deepcopy_reduce         | 2.62 us                                                               | 2.64 us: 1.01x slower                                                           |
| fannkuch                | 403 ms                                                                | 407 ms: 1.01x slower                                                            |
| json_dumps              | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                           |
| raytrace                | 254 ms                                                                | 256 ms: 1.01x slower                                                            |
| chaos                   | 57.9 ms                                                               | 58.6 ms: 1.01x slower                                                           |
| json                    | 5.05 ms                                                               | 5.13 ms: 1.02x slower                                                           |
| scimark_lu              | 111 ms                                                                | 114 ms: 1.02x slower                                                            |
| scimark_monte_carlo     | 66.1 ms                                                               | 68.3 ms: 1.03x slower                                                           |
| gc_traversal            | 3.51 ms                                                               | 3.78 ms: 1.08x slower                                                           |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (28): xml_etree_parse, typing_runtime_protocols, async_tree_cpu_io_mixed, sympy_expand, async_tree_cpu_io_mixed_tg, docutils, xml_etree_iterparse, dask, pylint, pycparser, bpe_tokeniser, asyncio_websockets, async_generators, sqlglot_normalize, sqlglot_optimize, float, async_tree_memoization_tg, coroutines, pyflate, bench_mp_pool, async_tree_memoization, coverage, async_tree_none, async_tree_io, sqlglot_parse, nbody, async_tree_io_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x