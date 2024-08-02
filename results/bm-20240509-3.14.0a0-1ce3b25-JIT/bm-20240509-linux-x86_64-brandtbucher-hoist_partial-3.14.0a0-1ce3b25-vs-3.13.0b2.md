# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: hoist_partial
- machine: linux-x86_64
- commit hash: 1ce3b25
- commit date: 2024-05-09
- overall geometric mean: 1.03x slower
- HPT reliability: 83.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                 |
| chameleon      | 7.22 ms                                                    | 7.17 ms: 1.01x faster                                                |
| docutils       | 2.83 sec                                                   | 2.98 sec: 1.05x slower                                               |
| html5lib       | 67.2 ms                                                    | 69.1 ms: 1.03x slower                                                |
| tornado_http   | 94.6 ms                                                    | 98.1 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                      | 1.03x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|--------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 363 ms: 1.04x faster                                                 |
| async_tree_none_tg | 336 ms                                                     | 345 ms: 1.03x slower                                                 |
| async_tree_io_tg   | 936 ms                                                     | 1.02 sec: 1.09x slower                                               |
| Geometric mean     | (ref)                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                |
| nbody          | 88.3 ms                                                    | 86.1 ms: 1.03x faster                                                |
| pidigits       | 191 ms                                                     | 197 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.04x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.58 ms: 1.03x faster                                                |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                                 |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                               |
| xml_etree_parse      | 162 ms                                                     | 152 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.05x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 33.1 us: 1.05x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                |
| xml_etree_generate   | 87.4 ms                                                    | 83.6 ms: 1.05x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                |
| unpickle_list        | 5.34 us                                                    | 5.27 us: 1.01x faster                                                |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.29 us: 1.04x slower                                                |
| pickle               | 11.5 us                                                    | 12.0 us: 1.05x slower                                                |
| unpickle             | 15.1 us                                                    | 15.9 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                         |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.70 ms: 1.08x slower                                                |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.62 ms: 1.17x faster                                                |
| django_template | 34.8 ms                                                    | 36.5 ms: 1.05x slower                                                |
| genshi_text     | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|--------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 321 ms: 1.22x faster                                                 |
| richards                 | 50.9 ms                                                    | 42.7 ms: 1.19x faster                                                |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.47 ms: 1.18x faster                                                |
| mako                     | 11.2 ms                                                    | 9.62 ms: 1.17x faster                                                |
| richards_super           | 57.4 ms                                                    | 49.1 ms: 1.17x faster                                                |
| spectral_norm            | 116 ms                                                     | 101 ms: 1.15x faster                                                 |
| float                    | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                |
| crypto_pyaes             | 77.5 ms                                                    | 69.6 ms: 1.11x faster                                                |
| fannkuch                 | 402 ms                                                     | 368 ms: 1.09x faster                                                 |
| tomli_loads              | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                               |
| scimark_monte_carlo      | 69.2 ms                                                    | 64.1 ms: 1.08x faster                                                |
| pyflate                  | 484 ms                                                     | 449 ms: 1.08x faster                                                 |
| xml_etree_parse          | 162 ms                                                     | 152 ms: 1.07x faster                                                 |
| deepcopy_memo            | 39.7 us                                                    | 37.5 us: 1.06x faster                                                |
| coverage                 | 93.1 ms                                                    | 88.2 ms: 1.06x faster                                                |
| xml_etree_iterparse      | 107 ms                                                     | 102 ms: 1.05x faster                                                 |
| pickle_dict              | 34.8 us                                                    | 33.1 us: 1.05x faster                                                |
| xml_etree_process        | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                |
| pprint_safe_repr         | 758 ms                                                     | 724 ms: 1.05x faster                                                 |
| xml_etree_generate       | 87.4 ms                                                    | 83.6 ms: 1.05x faster                                                |
| sqlite_synth             | 2.99 us                                                    | 2.86 us: 1.05x faster                                                |
| chaos                    | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                                |
| async_tree_none          | 378 ms                                                     | 363 ms: 1.04x faster                                                 |
| pprint_pformat           | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                               |
| json_dumps               | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                |
| regex_effbot             | 3.67 ms                                                    | 3.58 ms: 1.03x faster                                                |
| nbody                    | 88.3 ms                                                    | 86.1 ms: 1.03x faster                                                |
| mdp                      | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                               |
| coroutines               | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                |
| thrift                   | 823 us                                                     | 810 us: 1.02x faster                                                 |
| unpickle_list            | 5.34 us                                                    | 5.27 us: 1.01x faster                                                |
| logging_format           | 6.47 us                                                    | 6.40 us: 1.01x faster                                                |
| comprehensions           | 16.6 us                                                    | 16.4 us: 1.01x faster                                                |
| chameleon                | 7.22 ms                                                    | 7.17 ms: 1.01x faster                                                |
| logging_simple           | 5.74 us                                                    | 5.77 us: 1.00x slower                                                |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                               |
| sqlglot_transpile        | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                |
| create_gc_cycles         | 1.82 ms                                                    | 1.84 ms: 1.01x slower                                                |
| regex_compile            | 137 ms                                                     | 139 ms: 1.02x slower                                                 |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                 |
| generators               | 29.6 ms                                                    | 30.2 ms: 1.02x slower                                                |
| go                       | 145 ms                                                     | 148 ms: 1.02x slower                                                 |
| asyncio_tcp              | 508 ms                                                     | 519 ms: 1.02x slower                                                 |
| 2to3                     | 274 ms                                                     | 280 ms: 1.02x slower                                                 |
| logging_silent           | 105 ns                                                     | 107 ns: 1.02x slower                                                 |
| regex_dna                | 221 ms                                                     | 226 ms: 1.02x slower                                                 |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.02x slower                                                 |
| dask                     | 369 ms                                                     | 379 ms: 1.03x slower                                                 |
| html5lib                 | 67.2 ms                                                    | 69.1 ms: 1.03x slower                                                |
| async_tree_none_tg       | 336 ms                                                     | 345 ms: 1.03x slower                                                 |
| sqlglot_optimize         | 55.5 ms                                                    | 57.1 ms: 1.03x slower                                                |
| pidigits                 | 191 ms                                                     | 197 ms: 1.03x slower                                                 |
| gc_traversal             | 3.98 ms                                                    | 4.11 ms: 1.03x slower                                                |
| pathlib                  | 17.3 ms                                                    | 17.9 ms: 1.03x slower                                                |
| scimark_sor              | 127 ms                                                     | 132 ms: 1.03x slower                                                 |
| pickle_list              | 5.11 us                                                    | 5.29 us: 1.04x slower                                                |
| python_startup           | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                |
| tornado_http             | 94.6 ms                                                    | 98.1 ms: 1.04x slower                                                |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.04x slower                                                 |
| flaskblogging            | 9.01 ms                                                    | 9.37 ms: 1.04x slower                                                |
| deepcopy                 | 367 us                                                     | 383 us: 1.04x slower                                                 |
| bench_thread_pool        | 834 us                                                     | 871 us: 1.05x slower                                                 |
| dulwich_log              | 67.2 ms                                                    | 70.4 ms: 1.05x slower                                                |
| pickle                   | 11.5 us                                                    | 12.0 us: 1.05x slower                                                |
| django_template          | 34.8 ms                                                    | 36.5 ms: 1.05x slower                                                |
| unpickle                 | 15.1 us                                                    | 15.9 us: 1.05x slower                                                |
| docutils                 | 2.83 sec                                                   | 2.98 sec: 1.05x slower                                               |
| async_generators         | 442 ms                                                     | 468 ms: 1.06x slower                                                 |
| gunicorn                 | 1.28 ms                                                    | 1.35 ms: 1.06x slower                                                |
| hexiom                   | 6.30 ms                                                    | 6.69 ms: 1.06x slower                                                |
| raytrace                 | 267 ms                                                     | 284 ms: 1.06x slower                                                 |
| genshi_text              | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                |
| typing_runtime_protocols | 165 us                                                     | 176 us: 1.07x slower                                                 |
| aiohttp                  | 1.18 ms                                                    | 1.26 ms: 1.07x slower                                                |
| sympy_str                | 282 ms                                                     | 302 ms: 1.07x slower                                                 |
| nqueens                  | 81.4 ms                                                    | 87.7 ms: 1.08x slower                                                |
| sympy_expand             | 473 ms                                                     | 512 ms: 1.08x slower                                                 |
| python_startup_no_site   | 7.11 ms                                                    | 7.70 ms: 1.08x slower                                                |
| async_tree_io_tg         | 936 ms                                                     | 1.02 sec: 1.09x slower                                               |
| sympy_integrate          | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                |
| sympy_sum                | 156 ms                                                     | 174 ms: 1.12x slower                                                 |
| pylint                   | 317 ms                                                     | 357 ms: 1.13x slower                                                 |
| genshi_xml               | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                |
| deltablue                | 3.25 ms                                                    | 3.75 ms: 1.15x slower                                                |
| telco                    | 8.41 ms                                                    | 172 ms: 20.42x slower                                                |
| Geometric mean           | (ref)                                                      | 1.03x slower                                                         |

Benchmark hidden because not significant (15): async_tree_io, json_loads, pickle_pure_python, deepcopy_reduce, sqlglot_parse, regex_v8, async_tree_cpu_io_mixed_tg, asyncio_websockets, json, meteor_contest, pycparser, bench_mp_pool, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, djangocms, mypy2

# HPT report

- Reliability score: 83.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x