# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: peel
- machine: linux-x86_64
- commit hash: ee3b5e3
- commit date: 2024-05-10
- overall geometric mean: 1.03x slower
- HPT reliability: 70.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                        |
| chameleon      | 7.22 ms                                                    | 6.97 ms: 1.04x faster                                       |
| tornado_http   | 94.6 ms                                                    | 97.5 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                      | 1.00x slower                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|--------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 364 ms: 1.04x faster                                        |
| async_tree_none_tg | 336 ms                                                     | 347 ms: 1.03x slower                                        |
| async_tree_io_tg   | 936 ms                                                     | 985 ms: 1.05x slower                                        |
| Geometric mean     | (ref)                                                      | 1.02x slower                                                |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.2 ms: 1.11x faster                                       |
| nbody          | 88.3 ms                                                    | 83.9 ms: 1.05x faster                                       |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                      | 1.06x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.51 ms: 1.04x faster                                       |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                        |
| regex_v8       | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                       |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                      | 1.00x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 151 ms: 1.07x faster                                        |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.06x faster                                        |
| xml_etree_generate   | 87.4 ms                                                    | 83.3 ms: 1.05x faster                                       |
| xml_etree_process    | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                       |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                       |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                        |
| pickle_dict          | 34.8 us                                                    | 35.0 us: 1.01x slower                                       |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                       |
| unpickle_list        | 5.34 us                                                    | 5.52 us: 1.03x slower                                       |
| unpickle             | 15.1 us                                                    | 15.6 us: 1.03x slower                                       |
| unpickle_pure_python | 218 us                                                     | 227 us: 1.04x slower                                        |
| pickle_list          | 5.11 us                                                    | 5.60 us: 1.10x slower                                       |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.60 ms: 1.07x slower                                       |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.59 ms: 1.17x faster                                       |
| django_template | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                       |
| genshi_text     | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                       |
| genshi_xml      | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                       |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|--------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 319 ms: 1.23x faster                                        |
| richards                 | 50.9 ms                                                    | 41.5 ms: 1.23x faster                                       |
| richards_super           | 57.4 ms                                                    | 47.7 ms: 1.20x faster                                       |
| spectral_norm            | 116 ms                                                     | 97.1 ms: 1.20x faster                                       |
| mako                     | 11.2 ms                                                    | 9.59 ms: 1.17x faster                                       |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.58 ms: 1.15x faster                                       |
| crypto_pyaes             | 77.5 ms                                                    | 68.2 ms: 1.14x faster                                       |
| fannkuch                 | 402 ms                                                     | 359 ms: 1.12x faster                                        |
| float                    | 78.9 ms                                                    | 71.2 ms: 1.11x faster                                       |
| scimark_monte_carlo      | 69.2 ms                                                    | 63.0 ms: 1.10x faster                                       |
| tomli_loads              | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                      |
| pyflate                  | 484 ms                                                     | 449 ms: 1.08x faster                                        |
| mdp                      | 2.79 sec                                                   | 2.59 sec: 1.08x faster                                      |
| xml_etree_parse          | 162 ms                                                     | 151 ms: 1.07x faster                                        |
| xml_etree_iterparse      | 107 ms                                                     | 102 ms: 1.06x faster                                        |
| nbody                    | 88.3 ms                                                    | 83.9 ms: 1.05x faster                                       |
| deepcopy_memo            | 39.7 us                                                    | 37.8 us: 1.05x faster                                       |
| xml_etree_generate       | 87.4 ms                                                    | 83.3 ms: 1.05x faster                                       |
| sqlite_synth             | 2.99 us                                                    | 2.86 us: 1.05x faster                                       |
| regex_effbot             | 3.67 ms                                                    | 3.51 ms: 1.04x faster                                       |
| xml_etree_process        | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                       |
| async_tree_none          | 378 ms                                                     | 364 ms: 1.04x faster                                        |
| pprint_safe_repr         | 758 ms                                                     | 731 ms: 1.04x faster                                        |
| chameleon                | 7.22 ms                                                    | 6.97 ms: 1.04x faster                                       |
| json_dumps               | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                       |
| gc_traversal             | 3.98 ms                                                    | 3.90 ms: 1.02x faster                                       |
| pprint_pformat           | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                      |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                        |
| chaos                    | 61.3 ms                                                    | 60.5 ms: 1.01x faster                                       |
| pickle_pure_python       | 305 us                                                     | 301 us: 1.01x faster                                        |
| coverage                 | 93.1 ms                                                    | 92.0 ms: 1.01x faster                                       |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                       |
| comprehensions           | 16.6 us                                                    | 16.5 us: 1.01x faster                                       |
| json                     | 5.31 ms                                                    | 5.27 ms: 1.01x faster                                       |
| logging_format           | 6.47 us                                                    | 6.50 us: 1.01x slower                                       |
| logging_silent           | 105 ns                                                     | 105 ns: 1.01x slower                                        |
| pickle_dict              | 34.8 us                                                    | 35.0 us: 1.01x slower                                       |
| regex_dna                | 221 ms                                                     | 223 ms: 1.01x slower                                        |
| regex_v8                 | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                       |
| sqlglot_transpile        | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                       |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                      |
| bench_mp_pool            | 23.9 ms                                                    | 24.1 ms: 1.01x slower                                       |
| thrift                   | 823 us                                                     | 833 us: 1.01x slower                                        |
| python_startup           | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                       |
| go                       | 145 ms                                                     | 147 ms: 1.01x slower                                        |
| create_gc_cycles         | 1.82 ms                                                    | 1.84 ms: 1.01x slower                                       |
| logging_simple           | 5.74 us                                                    | 5.85 us: 1.02x slower                                       |
| 2to3                     | 274 ms                                                     | 279 ms: 1.02x slower                                        |
| meteor_contest           | 110 ms                                                     | 112 ms: 1.02x slower                                        |
| regex_compile            | 137 ms                                                     | 140 ms: 1.02x slower                                        |
| generators               | 29.6 ms                                                    | 30.3 ms: 1.02x slower                                       |
| pathlib                  | 17.3 ms                                                    | 17.7 ms: 1.02x slower                                       |
| asyncio_tcp              | 508 ms                                                     | 520 ms: 1.02x slower                                        |
| dulwich_log              | 67.2 ms                                                    | 68.8 ms: 1.02x slower                                       |
| flaskblogging            | 9.01 ms                                                    | 9.27 ms: 1.03x slower                                       |
| pickle                   | 11.5 us                                                    | 11.8 us: 1.03x slower                                       |
| dask                     | 369 ms                                                     | 380 ms: 1.03x slower                                        |
| tornado_http             | 94.6 ms                                                    | 97.5 ms: 1.03x slower                                       |
| sqlglot_optimize         | 55.5 ms                                                    | 57.2 ms: 1.03x slower                                       |
| async_tree_none_tg       | 336 ms                                                     | 347 ms: 1.03x slower                                        |
| unpickle_list            | 5.34 us                                                    | 5.52 us: 1.03x slower                                       |
| unpickle                 | 15.1 us                                                    | 15.6 us: 1.03x slower                                       |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.04x slower                                        |
| deepcopy                 | 367 us                                                     | 381 us: 1.04x slower                                        |
| unpickle_pure_python     | 218 us                                                     | 227 us: 1.04x slower                                        |
| typing_runtime_protocols | 165 us                                                     | 172 us: 1.04x slower                                        |
| django_template          | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                       |
| async_tree_io_tg         | 936 ms                                                     | 985 ms: 1.05x slower                                        |
| raytrace                 | 267 ms                                                     | 281 ms: 1.05x slower                                        |
| bench_thread_pool        | 834 us                                                     | 879 us: 1.05x slower                                        |
| nqueens                  | 81.4 ms                                                    | 85.9 ms: 1.06x slower                                       |
| async_generators         | 442 ms                                                     | 469 ms: 1.06x slower                                        |
| genshi_text              | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                       |
| python_startup_no_site   | 7.11 ms                                                    | 7.60 ms: 1.07x slower                                       |
| sympy_str                | 282 ms                                                     | 305 ms: 1.08x slower                                        |
| sympy_expand             | 473 ms                                                     | 510 ms: 1.08x slower                                        |
| hexiom                   | 6.30 ms                                                    | 6.80 ms: 1.08x slower                                       |
| pickle_list              | 5.11 us                                                    | 5.60 us: 1.10x slower                                       |
| sympy_sum                | 156 ms                                                     | 174 ms: 1.12x slower                                        |
| sympy_integrate          | 20.5 ms                                                    | 22.9 ms: 1.12x slower                                       |
| pylint                   | 317 ms                                                     | 356 ms: 1.12x slower                                        |
| genshi_xml               | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                       |
| deltablue                | 3.25 ms                                                    | 3.72 ms: 1.14x slower                                       |
| telco                    | 8.41 ms                                                    | 172 ms: 20.45x slower                                       |
| Geometric mean           | (ref)                                                      | 1.03x slower                                                |

Benchmark hidden because not significant (13): pycparser, html5lib, deepcopy_reduce, coroutines, scimark_sor, asyncio_websockets, json_loads, scimark_lu, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, docutils, gunicorn, mypy2

# HPT report

- Reliability score: 70.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x