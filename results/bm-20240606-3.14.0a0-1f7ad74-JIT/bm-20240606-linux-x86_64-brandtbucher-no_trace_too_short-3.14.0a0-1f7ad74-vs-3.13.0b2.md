# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_trace_too_short
- machine: linux-x86_64
- commit hash: 1f7ad74
- commit date: 2024-06-06
- overall geometric mean: 1.00x faster
- HPT reliability: 87.14%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                      |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                    |
| html5lib       | 67.2 ms                                                    | 69.5 ms: 1.03x slower                                                     |
| tornado_http   | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                      | 1.03x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|-------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 633 ms: 1.04x slower                                                      |
| Geometric mean          | (ref)                                                      | 1.01x slower                                                              |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 73.0 ms: 1.08x faster                                                     |
| nbody          | 88.3 ms                                                    | 81.8 ms: 1.08x faster                                                     |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                      | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                      |
| regex_v8       | 25.1 ms                                                    | 26.6 ms: 1.06x slower                                                     |
| regex_dna      | 221 ms                                                     | 238 ms: 1.07x slower                                                      |
| regex_effbot   | 3.67 ms                                                    | 4.01 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                      | 1.06x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.08x faster                                                      |
| xml_etree_generate   | 87.4 ms                                                    | 81.3 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                      |
| xml_etree_process    | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                     |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.02x faster                                                     |
| pickle_list          | 5.11 us                                                    | 5.05 us: 1.01x faster                                                     |
| unpickle_list        | 5.34 us                                                    | 5.43 us: 1.02x slower                                                     |
| unpickle_pure_python | 218 us                                                     | 223 us: 1.02x slower                                                      |
| pickle               | 11.5 us                                                    | 12.0 us: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                              |

Benchmark hidden because not significant (3): json_loads, pickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.62 ms: 1.07x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                     |
| django_template | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 318 ms: 1.23x faster                                                      |
| richards                 | 50.9 ms                                                    | 42.5 ms: 1.20x faster                                                     |
| richards_super           | 57.4 ms                                                    | 49.2 ms: 1.17x faster                                                     |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.55 ms: 1.16x faster                                                     |
| fannkuch                 | 402 ms                                                     | 350 ms: 1.15x faster                                                      |
| crypto_pyaes             | 77.5 ms                                                    | 67.9 ms: 1.14x faster                                                     |
| spectral_norm            | 116 ms                                                     | 102 ms: 1.14x faster                                                      |
| mako                     | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                     |
| scimark_monte_carlo      | 69.2 ms                                                    | 62.6 ms: 1.10x faster                                                     |
| tomli_loads              | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                    |
| pyflate                  | 484 ms                                                     | 446 ms: 1.08x faster                                                      |
| xml_etree_parse          | 162 ms                                                     | 149 ms: 1.08x faster                                                      |
| mdp                      | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                    |
| float                    | 78.9 ms                                                    | 73.0 ms: 1.08x faster                                                     |
| nbody                    | 88.3 ms                                                    | 81.8 ms: 1.08x faster                                                     |
| xml_etree_generate       | 87.4 ms                                                    | 81.3 ms: 1.07x faster                                                     |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.06x faster                                                      |
| sqlite_synth             | 2.99 us                                                    | 2.84 us: 1.05x faster                                                     |
| xml_etree_process        | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                     |
| pprint_safe_repr         | 758 ms                                                     | 724 ms: 1.05x faster                                                      |
| pathlib                  | 17.3 ms                                                    | 16.6 ms: 1.05x faster                                                     |
| pprint_pformat           | 1.56 sec                                                   | 1.49 sec: 1.04x faster                                                    |
| telco                    | 8.41 ms                                                    | 8.06 ms: 1.04x faster                                                     |
| json_dumps               | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                     |
| deepcopy_memo            | 39.7 us                                                    | 38.1 us: 1.04x faster                                                     |
| gc_traversal             | 3.98 ms                                                    | 3.83 ms: 1.04x faster                                                     |
| chaos                    | 61.3 ms                                                    | 59.4 ms: 1.03x faster                                                     |
| logging_format           | 6.47 us                                                    | 6.31 us: 1.03x faster                                                     |
| unpickle                 | 15.1 us                                                    | 14.9 us: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                      |
| logging_simple           | 5.74 us                                                    | 5.66 us: 1.01x faster                                                     |
| pickle_list              | 5.11 us                                                    | 5.05 us: 1.01x faster                                                     |
| coroutines               | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                     |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.01x faster                                                      |
| thrift                   | 823 us                                                     | 818 us: 1.01x faster                                                      |
| create_gc_cycles         | 1.82 ms                                                    | 1.81 ms: 1.00x faster                                                     |
| coverage                 | 93.1 ms                                                    | 93.8 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                                    |
| bench_mp_pool            | 23.9 ms                                                    | 24.1 ms: 1.01x slower                                                     |
| regex_compile            | 137 ms                                                     | 138 ms: 1.01x slower                                                      |
| sqlglot_transpile        | 1.63 ms                                                    | 1.66 ms: 1.01x slower                                                     |
| comprehensions           | 16.6 us                                                    | 16.8 us: 1.01x slower                                                     |
| json                     | 5.31 ms                                                    | 5.38 ms: 1.01x slower                                                     |
| unpickle_list            | 5.34 us                                                    | 5.43 us: 1.02x slower                                                     |
| deepcopy                 | 367 us                                                     | 373 us: 1.02x slower                                                      |
| asyncio_tcp              | 508 ms                                                     | 517 ms: 1.02x slower                                                      |
| dulwich_log              | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                     |
| 2to3                     | 274 ms                                                     | 280 ms: 1.02x slower                                                      |
| unpickle_pure_python     | 218 us                                                     | 223 us: 1.02x slower                                                      |
| go                       | 145 ms                                                     | 148 ms: 1.02x slower                                                      |
| tornado_http             | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                                     |
| dask                     | 369 ms                                                     | 379 ms: 1.03x slower                                                      |
| sqlglot_optimize         | 55.5 ms                                                    | 57.0 ms: 1.03x slower                                                     |
| generators               | 29.6 ms                                                    | 30.5 ms: 1.03x slower                                                     |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.03x slower                                                      |
| html5lib                 | 67.2 ms                                                    | 69.5 ms: 1.03x slower                                                     |
| typing_runtime_protocols | 165 us                                                     | 170 us: 1.03x slower                                                      |
| logging_silent           | 105 ns                                                     | 108 ns: 1.04x slower                                                      |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 633 ms: 1.04x slower                                                      |
| scimark_lu               | 122 ms                                                     | 126 ms: 1.04x slower                                                      |
| python_startup           | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                     |
| pickle                   | 11.5 us                                                    | 12.0 us: 1.04x slower                                                     |
| async_generators         | 442 ms                                                     | 462 ms: 1.04x slower                                                      |
| raytrace                 | 267 ms                                                     | 279 ms: 1.05x slower                                                      |
| hexiom                   | 6.30 ms                                                    | 6.59 ms: 1.05x slower                                                     |
| docutils                 | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                    |
| nqueens                  | 81.4 ms                                                    | 85.7 ms: 1.05x slower                                                     |
| pycparser                | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                                    |
| django_template          | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                     |
| genshi_text              | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                     |
| regex_v8                 | 25.1 ms                                                    | 26.6 ms: 1.06x slower                                                     |
| bench_thread_pool        | 834 us                                                     | 882 us: 1.06x slower                                                      |
| python_startup_no_site   | 7.11 ms                                                    | 7.62 ms: 1.07x slower                                                     |
| sympy_str                | 282 ms                                                     | 303 ms: 1.07x slower                                                      |
| regex_dna                | 221 ms                                                     | 238 ms: 1.07x slower                                                      |
| scimark_sor              | 127 ms                                                     | 138 ms: 1.08x slower                                                      |
| sympy_expand             | 473 ms                                                     | 515 ms: 1.09x slower                                                      |
| regex_effbot             | 3.67 ms                                                    | 4.01 ms: 1.09x slower                                                     |
| sympy_sum                | 156 ms                                                     | 172 ms: 1.10x slower                                                      |
| sympy_integrate          | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                     |
| pylint                   | 317 ms                                                     | 354 ms: 1.12x slower                                                      |
| genshi_xml               | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                     |
| deltablue                | 3.25 ms                                                    | 3.82 ms: 1.18x slower                                                     |
| Geometric mean           | (ref)                                                      | 1.00x faster                                                              |

Benchmark hidden because not significant (13): async_tree_io_tg, async_tree_none, json_loads, async_tree_memoization_tg, pickle_pure_python, sqlglot_parse, asyncio_websockets, deepcopy_reduce, async_tree_none_tg, async_tree_cpu_io_mixed_tg, pickle_dict, async_tree_io, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 87.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x