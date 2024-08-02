# Results vs. 3.13.0b2

- fork: python
- ref: 35b5eaa176a5bae8a0ca
- machine: linux-x86_64
- commit hash: 35b5eaa
- commit date: 2024-05-09
- overall geometric mean: 1.02x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.01x faster                                                  |
| chameleon      | 7.22 ms                                                    | 6.87 ms: 1.05x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.80 sec: 1.01x faster                                                |
| tornado_http   | 94.6 ms                                                    | 93.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|--------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 361 ms: 1.05x faster                                                  |
| async_tree_none_tg | 336 ms                                                     | 346 ms: 1.03x slower                                                  |
| async_tree_io_tg   | 936 ms                                                     | 983 ms: 1.05x slower                                                  |
| Geometric mean     | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 77.1 ms: 1.02x faster                                                 |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                 |
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                |
| pickle_dict          | 34.8 us                                                    | 33.9 us: 1.03x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 60.6 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.01x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 305 us: 1.00x faster                                                  |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.20 us: 1.02x slower                                                 |
| unpickle_list        | 5.34 us                                                    | 5.47 us: 1.02x slower                                                 |
| unpickle             | 15.1 us                                                    | 15.9 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.4 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.6 ms: 1.06x faster                                                 |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 50.9 ms: 1.01x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|-------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal            | 3.98 ms                                                    | 3.62 ms: 1.10x faster                                                 |
| richards_super          | 57.4 ms                                                    | 53.8 ms: 1.07x faster                                                 |
| richards                | 50.9 ms                                                    | 47.9 ms: 1.06x faster                                                 |
| mako                    | 11.2 ms                                                    | 10.6 ms: 1.06x faster                                                 |
| mdp                     | 2.79 sec                                                   | 2.63 sec: 1.06x faster                                                |
| scimark_fft             | 392 ms                                                     | 372 ms: 1.06x faster                                                  |
| chameleon               | 7.22 ms                                                    | 6.87 ms: 1.05x faster                                                 |
| crypto_pyaes            | 77.5 ms                                                    | 73.9 ms: 1.05x faster                                                 |
| async_tree_none         | 378 ms                                                     | 361 ms: 1.05x faster                                                  |
| scimark_lu              | 122 ms                                                     | 116 ms: 1.05x faster                                                  |
| python_startup          | 10.8 ms                                                    | 10.4 ms: 1.04x faster                                                 |
| hexiom                  | 6.30 ms                                                    | 6.11 ms: 1.03x faster                                                 |
| django_template         | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                 |
| tomli_loads             | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                |
| logging_format          | 6.47 us                                                    | 6.30 us: 1.03x faster                                                 |
| pickle_dict             | 34.8 us                                                    | 33.9 us: 1.03x faster                                                 |
| dulwich_log             | 67.2 ms                                                    | 65.6 ms: 1.02x faster                                                 |
| regex_v8                | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                 |
| float                   | 78.9 ms                                                    | 77.1 ms: 1.02x faster                                                 |
| chaos                   | 61.3 ms                                                    | 60.0 ms: 1.02x faster                                                 |
| pyflate                 | 484 ms                                                     | 474 ms: 1.02x faster                                                  |
| sqlglot_parse           | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                 |
| regex_compile           | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| sqlglot_transpile       | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 5.17 ms: 1.02x faster                                                 |
| logging_silent          | 105 ns                                                     | 103 ns: 1.02x faster                                                  |
| genshi_xml              | 51.6 ms                                                    | 50.9 ms: 1.01x faster                                                 |
| spectral_norm           | 116 ms                                                     | 114 ms: 1.01x faster                                                  |
| sqlite_synth            | 2.99 us                                                    | 2.95 us: 1.01x faster                                                 |
| 2to3                    | 274 ms                                                     | 270 ms: 1.01x faster                                                  |
| sqlglot_optimize        | 55.5 ms                                                    | 54.8 ms: 1.01x faster                                                 |
| scimark_monte_carlo     | 69.2 ms                                                    | 68.3 ms: 1.01x faster                                                 |
| deepcopy_reduce         | 3.35 us                                                    | 3.31 us: 1.01x faster                                                 |
| pidigits                | 191 ms                                                     | 189 ms: 1.01x faster                                                  |
| logging_simple          | 5.74 us                                                    | 5.68 us: 1.01x faster                                                 |
| fannkuch                | 402 ms                                                     | 398 ms: 1.01x faster                                                  |
| deepcopy_memo           | 39.7 us                                                    | 39.3 us: 1.01x faster                                                 |
| tornado_http            | 94.6 ms                                                    | 93.7 ms: 1.01x faster                                                 |
| go                      | 145 ms                                                     | 143 ms: 1.01x faster                                                  |
| docutils                | 2.83 sec                                                   | 2.80 sec: 1.01x faster                                                |
| genshi_text             | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                                 |
| xml_etree_process       | 61.2 ms                                                    | 60.6 ms: 1.01x faster                                                 |
| xml_etree_iterparse     | 107 ms                                                     | 106 ms: 1.01x faster                                                  |
| create_gc_cycles        | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                 |
| json_dumps              | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                 |
| generators              | 29.6 ms                                                    | 29.4 ms: 1.01x faster                                                 |
| asyncio_tcp             | 508 ms                                                     | 505 ms: 1.01x faster                                                  |
| asyncio_websockets      | 567 ms                                                     | 563 ms: 1.01x faster                                                  |
| raytrace                | 267 ms                                                     | 265 ms: 1.01x faster                                                  |
| unpickle_pure_python    | 218 us                                                     | 217 us: 1.01x faster                                                  |
| nqueens                 | 81.4 ms                                                    | 81.0 ms: 1.00x faster                                                 |
| comprehensions          | 16.6 us                                                    | 16.5 us: 1.00x faster                                                 |
| deepcopy                | 367 us                                                     | 366 us: 1.00x faster                                                  |
| sympy_integrate         | 20.5 ms                                                    | 20.4 ms: 1.00x faster                                                 |
| sqlglot_normalize       | 110 ms                                                     | 110 ms: 1.00x faster                                                  |
| pickle_pure_python      | 305 us                                                     | 305 us: 1.00x faster                                                  |
| bench_thread_pool       | 834 us                                                     | 832 us: 1.00x faster                                                  |
| meteor_contest          | 110 ms                                                     | 110 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                                |
| regex_dna               | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| pprint_pformat          | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                                |
| pprint_safe_repr        | 758 ms                                                     | 766 ms: 1.01x slower                                                  |
| async_generators        | 442 ms                                                     | 448 ms: 1.01x slower                                                  |
| pathlib                 | 17.3 ms                                                    | 17.6 ms: 1.01x slower                                                 |
| pickle                  | 11.5 us                                                    | 11.6 us: 1.01x slower                                                 |
| pickle_list             | 5.11 us                                                    | 5.20 us: 1.02x slower                                                 |
| coroutines              | 23.2 ms                                                    | 23.6 ms: 1.02x slower                                                 |
| unpickle_list           | 5.34 us                                                    | 5.47 us: 1.02x slower                                                 |
| json                    | 5.31 ms                                                    | 5.44 ms: 1.02x slower                                                 |
| scimark_sor             | 127 ms                                                     | 131 ms: 1.03x slower                                                  |
| async_tree_none_tg      | 336 ms                                                     | 346 ms: 1.03x slower                                                  |
| pycparser               | 1.16 sec                                                   | 1.20 sec: 1.03x slower                                                |
| unpickle                | 15.1 us                                                    | 15.9 us: 1.05x slower                                                 |
| async_tree_io_tg        | 936 ms                                                     | 983 ms: 1.05x slower                                                  |
| telco                   | 8.41 ms                                                    | 176 ms: 20.94x slower                                                 |
| Geometric mean          | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (23): flaskblogging, async_tree_io, bench_mp_pool, thrift, deltablue, html5lib, sympy_expand, xml_etree_parse, sympy_str, sympy_sum, xml_etree_generate, async_tree_cpu_io_mixed_tg, python_startup_no_site, regex_effbot, pylint, json_loads, dask, typing_runtime_protocols, coverage, nbody, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x