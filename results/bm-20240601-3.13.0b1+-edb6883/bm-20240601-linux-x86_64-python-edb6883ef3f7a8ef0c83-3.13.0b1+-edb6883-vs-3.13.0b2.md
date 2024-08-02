# Results vs. 3.13.0b2

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: linux-x86_64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                   |
| chameleon      | 7.22 ms                                                    | 6.89 ms: 1.05x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.84 sec: 1.00x slower                                                 |
| html5lib       | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                  |
| tornado_http   | 94.6 ms                                                    | 93.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                   |
| nbody          | 88.3 ms                                                    | 90.1 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 135 ms: 1.01x faster                                                   |
| regex_v8       | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                  |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_dict        | 34.8 us                                                    | 33.5 us: 1.04x faster                                                  |
| unpickle           | 15.1 us                                                    | 14.6 us: 1.03x faster                                                  |
| unpickle_list      | 5.34 us                                                    | 5.21 us: 1.03x faster                                                  |
| json_dumps         | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| pickle_pure_python | 305 us                                                     | 301 us: 1.01x faster                                                   |
| xml_etree_process  | 61.2 ms                                                    | 60.4 ms: 1.01x faster                                                  |
| xml_etree_generate | 87.4 ms                                                    | 86.4 ms: 1.01x faster                                                  |
| json_loads         | 28.9 us                                                    | 28.7 us: 1.01x faster                                                  |
| pickle_list        | 5.11 us                                                    | 5.08 us: 1.00x faster                                                  |
| pickle             | 11.5 us                                                    | 11.7 us: 1.02x slower                                                  |
| tomli_loads        | 2.12 sec                                                   | 2.17 sec: 1.03x slower                                                 |
| Geometric mean     | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                  |
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.8 ms: 1.04x faster                                                  |
| genshi_text     | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                  |
| genshi_xml      | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                  |
| django_template | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                     | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                 |
| chameleon               | 7.22 ms                                                    | 6.89 ms: 1.05x faster                                                  |
| scimark_fft             | 392 ms                                                     | 375 ms: 1.05x faster                                                   |
| mako                    | 11.2 ms                                                    | 10.8 ms: 1.04x faster                                                  |
| crypto_pyaes            | 77.5 ms                                                    | 74.4 ms: 1.04x faster                                                  |
| scimark_lu              | 122 ms                                                     | 117 ms: 1.04x faster                                                   |
| pickle_dict             | 34.8 us                                                    | 33.5 us: 1.04x faster                                                  |
| deepcopy_memo           | 39.7 us                                                    | 38.3 us: 1.04x faster                                                  |
| pyflate                 | 484 ms                                                     | 468 ms: 1.03x faster                                                   |
| unpickle                | 15.1 us                                                    | 14.6 us: 1.03x faster                                                  |
| gc_traversal            | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                                  |
| pprint_pformat          | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                 |
| genshi_text             | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                  |
| unpickle_list           | 5.34 us                                                    | 5.21 us: 1.03x faster                                                  |
| deepcopy                | 367 us                                                     | 358 us: 1.02x faster                                                   |
| nqueens                 | 81.4 ms                                                    | 79.5 ms: 1.02x faster                                                  |
| logging_silent          | 105 ns                                                     | 102 ns: 1.02x faster                                                   |
| deepcopy_reduce         | 3.35 us                                                    | 3.27 us: 1.02x faster                                                  |
| pprint_safe_repr        | 758 ms                                                     | 741 ms: 1.02x faster                                                   |
| genshi_xml              | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                  |
| scimark_monte_carlo     | 69.2 ms                                                    | 67.8 ms: 1.02x faster                                                  |
| chaos                   | 61.3 ms                                                    | 60.2 ms: 1.02x faster                                                  |
| json_dumps              | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| fannkuch                | 402 ms                                                     | 395 ms: 1.02x faster                                                   |
| coroutines              | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 5.19 ms: 1.02x faster                                                  |
| regex_compile           | 137 ms                                                     | 135 ms: 1.01x faster                                                   |
| logging_format          | 6.47 us                                                    | 6.38 us: 1.01x faster                                                  |
| pickle_pure_python      | 305 us                                                     | 301 us: 1.01x faster                                                   |
| pidigits                | 191 ms                                                     | 189 ms: 1.01x faster                                                   |
| generators              | 29.6 ms                                                    | 29.3 ms: 1.01x faster                                                  |
| xml_etree_process       | 61.2 ms                                                    | 60.4 ms: 1.01x faster                                                  |
| dulwich_log             | 67.2 ms                                                    | 66.4 ms: 1.01x faster                                                  |
| xml_etree_generate      | 87.4 ms                                                    | 86.4 ms: 1.01x faster                                                  |
| go                      | 145 ms                                                     | 143 ms: 1.01x faster                                                   |
| 2to3                    | 274 ms                                                     | 271 ms: 1.01x faster                                                   |
| sqlglot_transpile       | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                  |
| django_template         | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                  |
| tornado_http            | 94.6 ms                                                    | 93.8 ms: 1.01x faster                                                  |
| create_gc_cycles        | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                  |
| thrift                  | 823 us                                                     | 816 us: 1.01x faster                                                   |
| sqlglot_optimize        | 55.5 ms                                                    | 55.1 ms: 1.01x faster                                                  |
| json_loads              | 28.9 us                                                    | 28.7 us: 1.01x faster                                                  |
| sympy_integrate         | 20.5 ms                                                    | 20.4 ms: 1.01x faster                                                  |
| sympy_expand            | 473 ms                                                     | 470 ms: 1.01x faster                                                   |
| pickle_list             | 5.11 us                                                    | 5.08 us: 1.00x faster                                                  |
| richards_super          | 57.4 ms                                                    | 57.2 ms: 1.00x faster                                                  |
| async_generators        | 442 ms                                                     | 440 ms: 1.00x faster                                                   |
| python_startup_no_site  | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                  |
| python_startup          | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.84 sec: 1.00x slower                                                 |
| docutils                | 2.83 sec                                                   | 2.84 sec: 1.00x slower                                                 |
| scimark_sor             | 127 ms                                                     | 128 ms: 1.00x slower                                                   |
| deltablue               | 3.25 ms                                                    | 3.28 ms: 1.01x slower                                                  |
| comprehensions          | 16.6 us                                                    | 16.8 us: 1.01x slower                                                  |
| spectral_norm           | 116 ms                                                     | 118 ms: 1.01x slower                                                   |
| html5lib                | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                  |
| regex_v8                | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                  |
| raytrace                | 267 ms                                                     | 271 ms: 1.02x slower                                                   |
| pickle                  | 11.5 us                                                    | 11.7 us: 1.02x slower                                                  |
| nbody                   | 88.3 ms                                                    | 90.1 ms: 1.02x slower                                                  |
| regex_dna               | 221 ms                                                     | 226 ms: 1.02x slower                                                   |
| telco                   | 8.41 ms                                                    | 8.62 ms: 1.02x slower                                                  |
| tomli_loads             | 2.12 sec                                                   | 2.17 sec: 1.03x slower                                                 |
| pathlib                 | 17.3 ms                                                    | 17.8 ms: 1.03x slower                                                  |
| Geometric mean          | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (37): async_tree_none, async_tree_memoization, mypy2, flaskblogging, hexiom, pylint, async_tree_cpu_io_mixed_tg, coverage, sympy_str, djangocms, async_tree_cpu_io_mixed, richards, xml_etree_parse, json, dask, sympy_sum, float, sqlglot_parse, typing_runtime_protocols, async_tree_memoization_tg, gunicorn, meteor_contest, asyncio_websockets, async_tree_none_tg, unpickle_pure_python, asyncio_tcp, async_tree_io, pycparser, bench_thread_pool, aiohttp, bench_mp_pool, regex_effbot, sqlglot_normalize, xml_etree_iterparse, logging_simple, sqlite_synth, async_tree_io_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x