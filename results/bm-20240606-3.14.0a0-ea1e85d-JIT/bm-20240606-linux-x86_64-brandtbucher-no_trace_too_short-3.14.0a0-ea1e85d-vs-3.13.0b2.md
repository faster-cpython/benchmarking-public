# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_trace_too_short
- machine: linux-x86_64
- commit hash: ea1e85d
- commit date: 2024-06-06
- overall geometric mean: 1.00x faster
- HPT reliability: 76.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 281 ms: 1.03x slower                                                      |
| docutils       | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                    |
| html5lib       | 67.2 ms                                                    | 68.7 ms: 1.02x slower                                                     |
| tornado_http   | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                      | 1.03x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|-------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 939 ms                                                     | 979 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed | 611 ms                                                     | 637 ms: 1.04x slower                                                      |
| Geometric mean          | (ref)                                                      | 1.02x slower                                                              |

Benchmark hidden because not significant (6): async_tree_none, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                     |
| float          | 78.9 ms                                                    | 72.1 ms: 1.09x faster                                                     |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                      | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                     |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                      |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 81.4 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.05x faster                                                      |
| xml_etree_process    | 61.2 ms                                                    | 58.0 ms: 1.05x faster                                                     |
| unpickle_list        | 5.34 us                                                    | 5.20 us: 1.03x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.02x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                      |
| pickle_dict          | 34.8 us                                                    | 36.3 us: 1.04x slower                                                     |
| pickle_list          | 5.11 us                                                    | 5.34 us: 1.05x slower                                                     |
| pickle               | 11.5 us                                                    | 12.1 us: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.60 ms: 1.07x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.99 ms: 1.12x faster                                                     |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 59.8 ms: 1.16x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| richards                 | 50.9 ms                                                    | 41.5 ms: 1.23x faster                                                     |
| scimark_fft              | 392 ms                                                     | 327 ms: 1.20x faster                                                      |
| richards_super           | 57.4 ms                                                    | 47.9 ms: 1.20x faster                                                     |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.48 ms: 1.18x faster                                                     |
| spectral_norm            | 116 ms                                                     | 101 ms: 1.15x faster                                                      |
| fannkuch                 | 402 ms                                                     | 355 ms: 1.13x faster                                                      |
| crypto_pyaes             | 77.5 ms                                                    | 68.4 ms: 1.13x faster                                                     |
| mako                     | 11.2 ms                                                    | 9.99 ms: 1.12x faster                                                     |
| nbody                    | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                     |
| float                    | 78.9 ms                                                    | 72.1 ms: 1.09x faster                                                     |
| scimark_monte_carlo      | 69.2 ms                                                    | 63.3 ms: 1.09x faster                                                     |
| xml_etree_parse          | 162 ms                                                     | 150 ms: 1.08x faster                                                      |
| tomli_loads              | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                    |
| mdp                      | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                    |
| pyflate                  | 484 ms                                                     | 449 ms: 1.08x faster                                                      |
| pprint_pformat           | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                    |
| xml_etree_generate       | 87.4 ms                                                    | 81.4 ms: 1.07x faster                                                     |
| pprint_safe_repr         | 758 ms                                                     | 714 ms: 1.06x faster                                                      |
| xml_etree_iterparse      | 107 ms                                                     | 102 ms: 1.05x faster                                                      |
| xml_etree_process        | 61.2 ms                                                    | 58.0 ms: 1.05x faster                                                     |
| pathlib                  | 17.3 ms                                                    | 16.4 ms: 1.05x faster                                                     |
| sqlite_synth             | 2.99 us                                                    | 2.84 us: 1.05x faster                                                     |
| regex_v8                 | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                     |
| logging_format           | 6.47 us                                                    | 6.22 us: 1.04x faster                                                     |
| gc_traversal             | 3.98 ms                                                    | 3.84 ms: 1.04x faster                                                     |
| chaos                    | 61.3 ms                                                    | 59.3 ms: 1.04x faster                                                     |
| deepcopy_memo            | 39.7 us                                                    | 38.4 us: 1.03x faster                                                     |
| telco                    | 8.41 ms                                                    | 8.14 ms: 1.03x faster                                                     |
| unpickle_list            | 5.34 us                                                    | 5.20 us: 1.03x faster                                                     |
| coroutines               | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                     |
| json_dumps               | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| unpickle                 | 15.1 us                                                    | 14.9 us: 1.02x faster                                                     |
| meteor_contest           | 110 ms                                                     | 108 ms: 1.02x faster                                                      |
| sqlglot_parse            | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                      |
| logging_simple           | 5.74 us                                                    | 5.65 us: 1.02x faster                                                     |
| create_gc_cycles         | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                     |
| pickle_pure_python       | 305 us                                                     | 303 us: 1.01x faster                                                      |
| comprehensions           | 16.6 us                                                    | 16.7 us: 1.00x slower                                                     |
| regex_compile            | 137 ms                                                     | 138 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.87 sec: 1.01x slower                                                    |
| deepcopy                 | 367 us                                                     | 372 us: 1.01x slower                                                      |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                      |
| regex_dna                | 221 ms                                                     | 226 ms: 1.02x slower                                                      |
| logging_silent           | 105 ns                                                     | 107 ns: 1.02x slower                                                      |
| html5lib                 | 67.2 ms                                                    | 68.7 ms: 1.02x slower                                                     |
| dask                     | 369 ms                                                     | 378 ms: 1.02x slower                                                      |
| json                     | 5.31 ms                                                    | 5.43 ms: 1.02x slower                                                     |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.03x slower                                                      |
| tornado_http             | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                                     |
| dulwich_log              | 67.2 ms                                                    | 68.9 ms: 1.03x slower                                                     |
| 2to3                     | 274 ms                                                     | 281 ms: 1.03x slower                                                      |
| asyncio_tcp              | 508 ms                                                     | 523 ms: 1.03x slower                                                      |
| sqlglot_optimize         | 55.5 ms                                                    | 57.3 ms: 1.03x slower                                                     |
| go                       | 145 ms                                                     | 149 ms: 1.03x slower                                                      |
| typing_runtime_protocols | 165 us                                                     | 170 us: 1.03x slower                                                      |
| python_startup           | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                     |
| docutils                 | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                    |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.04x slower                                                      |
| django_template          | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                     |
| async_tree_io            | 939 ms                                                     | 979 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 637 ms: 1.04x slower                                                      |
| raytrace                 | 267 ms                                                     | 278 ms: 1.04x slower                                                      |
| pickle_dict              | 34.8 us                                                    | 36.3 us: 1.04x slower                                                     |
| pickle_list              | 5.11 us                                                    | 5.34 us: 1.05x slower                                                     |
| async_generators         | 442 ms                                                     | 462 ms: 1.05x slower                                                      |
| bench_thread_pool        | 834 us                                                     | 878 us: 1.05x slower                                                      |
| hexiom                   | 6.30 ms                                                    | 6.64 ms: 1.05x slower                                                     |
| genshi_text              | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                     |
| pickle                   | 11.5 us                                                    | 12.1 us: 1.06x slower                                                     |
| sympy_str                | 282 ms                                                     | 302 ms: 1.07x slower                                                      |
| nqueens                  | 81.4 ms                                                    | 86.9 ms: 1.07x slower                                                     |
| python_startup_no_site   | 7.11 ms                                                    | 7.60 ms: 1.07x slower                                                     |
| scimark_sor              | 127 ms                                                     | 137 ms: 1.08x slower                                                      |
| sympy_expand             | 473 ms                                                     | 511 ms: 1.08x slower                                                      |
| sympy_sum                | 156 ms                                                     | 171 ms: 1.10x slower                                                      |
| sympy_integrate          | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                     |
| pylint                   | 317 ms                                                     | 357 ms: 1.13x slower                                                      |
| genshi_xml               | 51.6 ms                                                    | 59.8 ms: 1.16x slower                                                     |
| deltablue                | 3.25 ms                                                    | 3.78 ms: 1.16x slower                                                     |
| generators               | 29.6 ms                                                    | 49.4 ms: 1.67x slower                                                     |
| Geometric mean           | (ref)                                                      | 1.00x faster                                                              |

Benchmark hidden because not significant (15): pycparser, async_tree_none, async_tree_io_tg, coverage, async_tree_memoization_tg, sqlglot_transpile, thrift, asyncio_websockets, regex_effbot, bench_mp_pool, json_loads, deepcopy_reduce, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 76.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x