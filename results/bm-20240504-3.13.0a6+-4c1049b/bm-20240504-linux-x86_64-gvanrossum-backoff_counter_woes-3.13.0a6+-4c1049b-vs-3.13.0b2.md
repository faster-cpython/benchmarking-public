# Results vs. 3.13.0b2

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-x86_64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x slower
- HPT reliability: 51.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                       |
| chameleon      | 7.22 ms                                                    | 7.15 ms: 1.01x faster                                                      |
| html5lib       | 67.2 ms                                                    | 68.8 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 628 ms: 1.03x slower                                                       |
| async_tree_none_tg      | 336 ms                                                     | 349 ms: 1.04x slower                                                       |
| Geometric mean          | (ref)                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (6): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 78.5 ms: 1.00x faster                                                      |
| nbody          | 88.3 ms                                                    | 90.4 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                      |
| regex_v8       | 25.1 ms                                                    | 26.0 ms: 1.04x slower                                                      |
| regex_dna      | 221 ms                                                     | 232 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                      | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| pickle_list          | 5.11 us                                                    | 5.00 us: 1.02x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.02x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 88.1 ms: 1.01x slower                                                      |
| unpickle             | 15.1 us                                                    | 15.3 us: 1.01x slower                                                      |
| unpickle_list        | 5.34 us                                                    | 5.44 us: 1.02x slower                                                      |
| pickle_pure_python   | 305 us                                                     | 314 us: 1.03x slower                                                       |
| tomli_loads          | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                     |
| unpickle_pure_python | 218 us                                                     | 225 us: 1.03x slower                                                       |
| pickle               | 11.5 us                                                    | 12.0 us: 1.05x slower                                                      |
| pickle_dict          | 34.8 us                                                    | 36.4 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.21 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                      | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.7 ms: 1.05x faster                                                      |
| genshi_text     | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                      |
| django_template | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 52.2 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| spectral_norm            | 116 ms                                                     | 110 ms: 1.06x faster                                                       |
| scimark_fft              | 392 ms                                                     | 372 ms: 1.05x faster                                                       |
| mdp                      | 2.79 sec                                                   | 2.65 sec: 1.05x faster                                                     |
| mako                     | 11.2 ms                                                    | 10.7 ms: 1.05x faster                                                      |
| chaos                    | 61.3 ms                                                    | 58.9 ms: 1.04x faster                                                      |
| json_loads               | 28.9 us                                                    | 27.7 us: 1.04x faster                                                      |
| genshi_text              | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                      |
| sqlite_synth             | 2.99 us                                                    | 2.90 us: 1.03x faster                                                      |
| pyflate                  | 484 ms                                                     | 474 ms: 1.02x faster                                                       |
| json_dumps               | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| pickle_list              | 5.11 us                                                    | 5.00 us: 1.02x faster                                                      |
| xml_etree_parse          | 162 ms                                                     | 158 ms: 1.02x faster                                                       |
| logging_silent           | 105 ns                                                     | 103 ns: 1.02x faster                                                       |
| hexiom                   | 6.30 ms                                                    | 6.18 ms: 1.02x faster                                                      |
| deepcopy_reduce          | 3.35 us                                                    | 3.29 us: 1.02x faster                                                      |
| richards_super           | 57.4 ms                                                    | 56.4 ms: 1.02x faster                                                      |
| meteor_contest           | 110 ms                                                     | 108 ms: 1.01x faster                                                       |
| deepcopy                 | 367 us                                                     | 363 us: 1.01x faster                                                       |
| generators               | 29.6 ms                                                    | 29.3 ms: 1.01x faster                                                      |
| scimark_lu               | 122 ms                                                     | 120 ms: 1.01x faster                                                       |
| richards                 | 50.9 ms                                                    | 50.4 ms: 1.01x faster                                                      |
| chameleon                | 7.22 ms                                                    | 7.15 ms: 1.01x faster                                                      |
| 2to3                     | 274 ms                                                     | 272 ms: 1.01x faster                                                       |
| dulwich_log              | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                                      |
| crypto_pyaes             | 77.5 ms                                                    | 76.9 ms: 1.01x faster                                                      |
| thrift                   | 823 us                                                     | 818 us: 1.01x faster                                                       |
| pprint_pformat           | 1.56 sec                                                   | 1.55 sec: 1.01x faster                                                     |
| float                    | 78.9 ms                                                    | 78.5 ms: 1.00x faster                                                      |
| raytrace                 | 267 ms                                                     | 265 ms: 1.00x faster                                                       |
| python_startup           | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                                      |
| pprint_safe_repr         | 758 ms                                                     | 755 ms: 1.00x faster                                                       |
| asyncio_tcp              | 508 ms                                                     | 506 ms: 1.00x faster                                                       |
| fannkuch                 | 402 ms                                                     | 401 ms: 1.00x faster                                                       |
| gc_traversal             | 3.98 ms                                                    | 3.99 ms: 1.00x slower                                                      |
| scimark_sor              | 127 ms                                                     | 128 ms: 1.00x slower                                                       |
| async_generators         | 442 ms                                                     | 444 ms: 1.00x slower                                                       |
| sqlglot_transpile        | 1.63 ms                                                    | 1.64 ms: 1.01x slower                                                      |
| scimark_monte_carlo      | 69.2 ms                                                    | 69.6 ms: 1.01x slower                                                      |
| xml_etree_generate       | 87.4 ms                                                    | 88.1 ms: 1.01x slower                                                      |
| gunicorn                 | 1.28 ms                                                    | 1.29 ms: 1.01x slower                                                      |
| aiohttp                  | 1.18 ms                                                    | 1.19 ms: 1.01x slower                                                      |
| django_template          | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                      |
| sympy_expand             | 473 ms                                                     | 477 ms: 1.01x slower                                                       |
| pathlib                  | 17.3 ms                                                    | 17.5 ms: 1.01x slower                                                      |
| deltablue                | 3.25 ms                                                    | 3.29 ms: 1.01x slower                                                      |
| genshi_xml               | 51.6 ms                                                    | 52.2 ms: 1.01x slower                                                      |
| coroutines               | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                                      |
| comprehensions           | 16.6 us                                                    | 16.8 us: 1.01x slower                                                      |
| deepcopy_memo            | 39.7 us                                                    | 40.2 us: 1.01x slower                                                      |
| logging_simple           | 5.74 us                                                    | 5.82 us: 1.01x slower                                                      |
| unpickle                 | 15.1 us                                                    | 15.3 us: 1.01x slower                                                      |
| python_startup_no_site   | 7.11 ms                                                    | 7.21 ms: 1.01x slower                                                      |
| create_gc_cycles         | 1.82 ms                                                    | 1.84 ms: 1.01x slower                                                      |
| coverage                 | 93.1 ms                                                    | 94.7 ms: 1.02x slower                                                      |
| unpickle_list            | 5.34 us                                                    | 5.44 us: 1.02x slower                                                      |
| sqlglot_normalize        | 110 ms                                                     | 112 ms: 1.02x slower                                                       |
| typing_runtime_protocols | 165 us                                                     | 168 us: 1.02x slower                                                       |
| telco                    | 8.41 ms                                                    | 8.60 ms: 1.02x slower                                                      |
| nbody                    | 88.3 ms                                                    | 90.4 ms: 1.02x slower                                                      |
| html5lib                 | 67.2 ms                                                    | 68.8 ms: 1.02x slower                                                      |
| nqueens                  | 81.4 ms                                                    | 83.4 ms: 1.02x slower                                                      |
| pickle_pure_python       | 305 us                                                     | 314 us: 1.03x slower                                                       |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 628 ms: 1.03x slower                                                       |
| tomli_loads              | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                     |
| regex_effbot             | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                      |
| unpickle_pure_python     | 218 us                                                     | 225 us: 1.03x slower                                                       |
| regex_v8                 | 25.1 ms                                                    | 26.0 ms: 1.04x slower                                                      |
| async_tree_none_tg       | 336 ms                                                     | 349 ms: 1.04x slower                                                       |
| pickle                   | 11.5 us                                                    | 12.0 us: 1.05x slower                                                      |
| regex_dna                | 221 ms                                                     | 232 ms: 1.05x slower                                                       |
| pickle_dict              | 34.8 us                                                    | 36.4 us: 1.05x slower                                                      |
| Geometric mean           | (ref)                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (31): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, xml_etree_process, sympy_integrate, logging_format, go, asyncio_websockets, bench_thread_pool, sqlglot_optimize, pidigits, bench_mp_pool, tornado_http, regex_compile, flaskblogging, json, asyncio_tcp_ssl, xml_etree_iterparse, sympy_sum, dask, sympy_str, docutils, async_tree_io, mypy2, scimark_sparse_mat_mult, sqlglot_parse, async_tree_memoization, async_tree_memoization_tg, pycparser, djangocms, pylint
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 51.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x