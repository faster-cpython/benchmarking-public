# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: hoist
- machine: linux-x86_64
- commit hash: 5e272c0
- commit date: 2024-05-09
- overall geometric mean: 1.03x slower
- HPT reliability: 86.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                         |
| chameleon      | 7.22 ms                                                    | 7.17 ms: 1.01x faster                                        |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                       |
| html5lib       | 67.2 ms                                                    | 69.2 ms: 1.03x slower                                        |
| tornado_http   | 94.6 ms                                                    | 97.9 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                      | 1.03x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|--------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 368 ms: 1.03x faster                                         |
| async_tree_none_tg | 336 ms                                                     | 350 ms: 1.04x slower                                         |
| async_tree_io_tg   | 936 ms                                                     | 1.02 sec: 1.09x slower                                       |
| Geometric mean     | (ref)                                                      | 1.02x slower                                                 |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.3 ms: 1.11x faster                                        |
| nbody          | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                        |
| pidigits       | 191 ms                                                     | 197 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                      | 1.05x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 220 ms: 1.00x faster                                         |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                        |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                         |
| regex_effbot   | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                      | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                       |
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.06x faster                                         |
| xml_etree_generate   | 87.4 ms                                                    | 83.4 ms: 1.05x faster                                        |
| xml_etree_process    | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                        |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                        |
| pickle_dict          | 34.8 us                                                    | 34.2 us: 1.02x faster                                        |
| unpickle_list        | 5.34 us                                                    | 5.25 us: 1.02x faster                                        |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.01x faster                                         |
| unpickle_pure_python | 218 us                                                     | 223 us: 1.02x slower                                         |
| unpickle             | 15.1 us                                                    | 16.0 us: 1.06x slower                                        |
| pickle               | 11.5 us                                                    | 12.2 us: 1.06x slower                                        |
| pickle_list          | 5.11 us                                                    | 5.47 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                 |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                        |
| python_startup_no_site | 7.11 ms                                                    | 7.65 ms: 1.08x slower                                        |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.53 ms: 1.18x faster                                        |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                        |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                        |
| genshi_xml      | 51.6 ms                                                    | 57.4 ms: 1.11x slower                                        |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|--------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 323 ms: 1.21x faster                                         |
| richards                 | 50.9 ms                                                    | 42.6 ms: 1.19x faster                                        |
| mako                     | 11.2 ms                                                    | 9.53 ms: 1.18x faster                                        |
| richards_super           | 57.4 ms                                                    | 48.7 ms: 1.18x faster                                        |
| spectral_norm            | 116 ms                                                     | 99.0 ms: 1.17x faster                                        |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.56 ms: 1.16x faster                                        |
| crypto_pyaes             | 77.5 ms                                                    | 69.4 ms: 1.12x faster                                        |
| float                    | 78.9 ms                                                    | 71.3 ms: 1.11x faster                                        |
| fannkuch                 | 402 ms                                                     | 365 ms: 1.10x faster                                         |
| nbody                    | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                        |
| pyflate                  | 484 ms                                                     | 444 ms: 1.09x faster                                         |
| tomli_loads              | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                       |
| xml_etree_parse          | 162 ms                                                     | 150 ms: 1.08x faster                                         |
| scimark_monte_carlo      | 69.2 ms                                                    | 64.5 ms: 1.07x faster                                        |
| coverage                 | 93.1 ms                                                    | 87.1 ms: 1.07x faster                                        |
| deepcopy_memo            | 39.7 us                                                    | 37.5 us: 1.06x faster                                        |
| xml_etree_iterparse      | 107 ms                                                     | 102 ms: 1.06x faster                                         |
| chaos                    | 61.3 ms                                                    | 58.4 ms: 1.05x faster                                        |
| xml_etree_generate       | 87.4 ms                                                    | 83.4 ms: 1.05x faster                                        |
| xml_etree_process        | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                        |
| sqlite_synth             | 2.99 us                                                    | 2.86 us: 1.05x faster                                        |
| json_dumps               | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                        |
| pprint_safe_repr         | 758 ms                                                     | 730 ms: 1.04x faster                                         |
| pprint_pformat           | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                       |
| deepcopy_reduce          | 3.35 us                                                    | 3.26 us: 1.03x faster                                        |
| async_tree_none          | 378 ms                                                     | 368 ms: 1.03x faster                                         |
| pickle_dict              | 34.8 us                                                    | 34.2 us: 1.02x faster                                        |
| unpickle_list            | 5.34 us                                                    | 5.25 us: 1.02x faster                                        |
| thrift                   | 823 us                                                     | 814 us: 1.01x faster                                         |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.01x faster                                         |
| chameleon                | 7.22 ms                                                    | 7.17 ms: 1.01x faster                                        |
| pickle_pure_python       | 305 us                                                     | 304 us: 1.01x faster                                         |
| coroutines               | 23.2 ms                                                    | 23.1 ms: 1.01x faster                                        |
| regex_dna                | 221 ms                                                     | 220 ms: 1.00x faster                                         |
| create_gc_cycles         | 1.82 ms                                                    | 1.82 ms: 1.00x slower                                        |
| deepcopy                 | 367 us                                                     | 369 us: 1.01x slower                                         |
| sqlglot_transpile        | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                        |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                       |
| gc_traversal             | 3.98 ms                                                    | 4.01 ms: 1.01x slower                                        |
| mdp                      | 2.79 sec                                                   | 2.81 sec: 1.01x slower                                       |
| go                       | 145 ms                                                     | 146 ms: 1.01x slower                                         |
| scimark_sor              | 127 ms                                                     | 129 ms: 1.01x slower                                         |
| generators               | 29.6 ms                                                    | 29.9 ms: 1.01x slower                                        |
| regex_v8                 | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                        |
| logging_silent           | 105 ns                                                     | 106 ns: 1.01x slower                                         |
| regex_compile            | 137 ms                                                     | 139 ms: 1.02x slower                                         |
| unpickle_pure_python     | 218 us                                                     | 223 us: 1.02x slower                                         |
| 2to3                     | 274 ms                                                     | 280 ms: 1.02x slower                                         |
| asyncio_tcp              | 508 ms                                                     | 521 ms: 1.02x slower                                         |
| dask                     | 369 ms                                                     | 379 ms: 1.03x slower                                         |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.03x slower                                         |
| raytrace                 | 267 ms                                                     | 274 ms: 1.03x slower                                         |
| sqlglot_optimize         | 55.5 ms                                                    | 57.1 ms: 1.03x slower                                        |
| pidigits                 | 191 ms                                                     | 197 ms: 1.03x slower                                         |
| html5lib                 | 67.2 ms                                                    | 69.2 ms: 1.03x slower                                        |
| pathlib                  | 17.3 ms                                                    | 17.9 ms: 1.03x slower                                        |
| python_startup           | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                        |
| tornado_http             | 94.6 ms                                                    | 97.9 ms: 1.03x slower                                        |
| flaskblogging            | 9.01 ms                                                    | 9.32 ms: 1.03x slower                                        |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.04x slower                                         |
| pycparser                | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                       |
| regex_effbot             | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                        |
| async_tree_none_tg       | 336 ms                                                     | 350 ms: 1.04x slower                                         |
| bench_thread_pool        | 834 us                                                     | 869 us: 1.04x slower                                         |
| genshi_text              | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                        |
| dulwich_log              | 67.2 ms                                                    | 70.5 ms: 1.05x slower                                        |
| docutils                 | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                       |
| django_template          | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                        |
| unpickle                 | 15.1 us                                                    | 16.0 us: 1.06x slower                                        |
| gunicorn                 | 1.28 ms                                                    | 1.36 ms: 1.06x slower                                        |
| aiohttp                  | 1.18 ms                                                    | 1.25 ms: 1.06x slower                                        |
| pickle                   | 11.5 us                                                    | 12.2 us: 1.06x slower                                        |
| typing_runtime_protocols | 165 us                                                     | 176 us: 1.07x slower                                         |
| async_generators         | 442 ms                                                     | 472 ms: 1.07x slower                                         |
| pickle_list              | 5.11 us                                                    | 5.47 us: 1.07x slower                                        |
| sympy_expand             | 473 ms                                                     | 507 ms: 1.07x slower                                         |
| python_startup_no_site   | 7.11 ms                                                    | 7.65 ms: 1.08x slower                                        |
| sympy_str                | 282 ms                                                     | 304 ms: 1.08x slower                                         |
| nqueens                  | 81.4 ms                                                    | 87.7 ms: 1.08x slower                                        |
| async_tree_io_tg         | 936 ms                                                     | 1.02 sec: 1.09x slower                                       |
| hexiom                   | 6.30 ms                                                    | 6.85 ms: 1.09x slower                                        |
| genshi_xml               | 51.6 ms                                                    | 57.4 ms: 1.11x slower                                        |
| sympy_integrate          | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                        |
| sympy_sum                | 156 ms                                                     | 174 ms: 1.12x slower                                         |
| pylint                   | 317 ms                                                     | 357 ms: 1.12x slower                                         |
| deltablue                | 3.25 ms                                                    | 3.74 ms: 1.15x slower                                        |
| telco                    | 8.41 ms                                                    | 173 ms: 20.53x slower                                        |
| Geometric mean           | (ref)                                                      | 1.03x slower                                                 |

Benchmark hidden because not significant (13): json, async_tree_io, sqlglot_parse, json_loads, comprehensions, asyncio_websockets, logging_format, bench_mp_pool, logging_simple, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, djangocms, mypy2

# HPT report

- Reliability score: 86.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x