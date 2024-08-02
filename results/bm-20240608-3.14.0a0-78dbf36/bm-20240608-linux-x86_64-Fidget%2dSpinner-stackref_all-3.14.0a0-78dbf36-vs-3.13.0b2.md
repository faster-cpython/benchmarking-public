# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 78dbf36
- commit date: 2024-06-08
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 268 ms: 1.02x faster                                                    |
| docutils       | 2.83 sec                                                   | 2.77 sec: 1.02x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 93.8 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|-------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 631 ms: 1.03x slower                                                    |
| Geometric mean          | (ref)                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 86.3 ms: 1.02x faster                                                   |
| float          | 78.9 ms                                                    | 77.9 ms: 1.01x faster                                                   |
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.03x faster                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.80 ms: 1.03x slower                                                   |
| regex_v8       | 25.1 ms                                                    | 26.0 ms: 1.04x slower                                                   |
| regex_dna      | 221 ms                                                     | 233 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                      | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.03x faster                                                    |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 59.6 ms: 1.03x faster                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 85.6 ms: 1.02x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 299 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                                                    |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                    |
| unpickle_list        | 5.34 us                                                    | 5.31 us: 1.01x faster                                                   |
| pickle_dict          | 34.8 us                                                    | 35.2 us: 1.01x slower                                                   |
| tomli_loads          | 2.12 sec                                                   | 2.15 sec: 1.01x slower                                                  |
| pickle_list          | 5.11 us                                                    | 5.18 us: 1.02x slower                                                   |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 50.1 ms: 1.03x faster                                                   |
| genshi_text     | 23.7 ms                                                    | 23.2 ms: 1.02x faster                                                   |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                   |
| mako            | 11.2 ms                                                    | 11.2 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|-------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                     | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                  |
| pathlib                 | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                   |
| richards                | 50.9 ms                                                    | 47.4 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 4.92 ms: 1.07x faster                                                   |
| richards_super          | 57.4 ms                                                    | 54.0 ms: 1.06x faster                                                   |
| scimark_fft             | 392 ms                                                     | 376 ms: 1.04x faster                                                    |
| scimark_lu              | 122 ms                                                     | 117 ms: 1.04x faster                                                    |
| logging_format          | 6.47 us                                                    | 6.24 us: 1.04x faster                                                   |
| xml_etree_parse         | 162 ms                                                     | 156 ms: 1.03x faster                                                    |
| regex_compile           | 137 ms                                                     | 132 ms: 1.03x faster                                                    |
| chaos                   | 61.3 ms                                                    | 59.3 ms: 1.03x faster                                                   |
| deepcopy_reduce         | 3.35 us                                                    | 3.24 us: 1.03x faster                                                   |
| json_dumps              | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                   |
| dulwich_log             | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                   |
| genshi_xml              | 51.6 ms                                                    | 50.1 ms: 1.03x faster                                                   |
| crypto_pyaes            | 77.5 ms                                                    | 75.2 ms: 1.03x faster                                                   |
| xml_etree_process       | 61.2 ms                                                    | 59.6 ms: 1.03x faster                                                   |
| nqueens                 | 81.4 ms                                                    | 79.3 ms: 1.03x faster                                                   |
| nbody                   | 88.3 ms                                                    | 86.3 ms: 1.02x faster                                                   |
| pyflate                 | 484 ms                                                     | 473 ms: 1.02x faster                                                    |
| generators              | 29.6 ms                                                    | 29.0 ms: 1.02x faster                                                   |
| 2to3                    | 274 ms                                                     | 268 ms: 1.02x faster                                                    |
| xml_etree_generate      | 87.4 ms                                                    | 85.6 ms: 1.02x faster                                                   |
| logging_simple          | 5.74 us                                                    | 5.62 us: 1.02x faster                                                   |
| scimark_monte_carlo     | 69.2 ms                                                    | 67.7 ms: 1.02x faster                                                   |
| go                      | 145 ms                                                     | 142 ms: 1.02x faster                                                    |
| thrift                  | 823 us                                                     | 806 us: 1.02x faster                                                    |
| meteor_contest          | 110 ms                                                     | 108 ms: 1.02x faster                                                    |
| pickle_pure_python      | 305 us                                                     | 299 us: 1.02x faster                                                    |
| sqlite_synth            | 2.99 us                                                    | 2.93 us: 1.02x faster                                                   |
| docutils                | 2.83 sec                                                   | 2.77 sec: 1.02x faster                                                  |
| pprint_safe_repr        | 758 ms                                                     | 744 ms: 1.02x faster                                                    |
| pprint_pformat          | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                                  |
| genshi_text             | 23.7 ms                                                    | 23.2 ms: 1.02x faster                                                   |
| create_gc_cycles        | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                   |
| sympy_str               | 282 ms                                                     | 277 ms: 1.02x faster                                                    |
| hexiom                  | 6.30 ms                                                    | 6.19 ms: 1.02x faster                                                   |
| spectral_norm           | 116 ms                                                     | 114 ms: 1.02x faster                                                    |
| django_template         | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                   |
| xml_etree_iterparse     | 107 ms                                                     | 106 ms: 1.01x faster                                                    |
| deepcopy                | 367 us                                                     | 362 us: 1.01x faster                                                    |
| asyncio_tcp             | 508 ms                                                     | 501 ms: 1.01x faster                                                    |
| sqlglot_transpile       | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                                   |
| sqlglot_optimize        | 55.5 ms                                                    | 54.8 ms: 1.01x faster                                                   |
| float                   | 78.9 ms                                                    | 77.9 ms: 1.01x faster                                                   |
| scimark_sor             | 127 ms                                                     | 126 ms: 1.01x faster                                                    |
| python_startup          | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                   |
| raytrace                | 267 ms                                                     | 264 ms: 1.01x faster                                                    |
| coverage                | 93.1 ms                                                    | 92.1 ms: 1.01x faster                                                   |
| sympy_integrate         | 20.5 ms                                                    | 20.3 ms: 1.01x faster                                                   |
| deepcopy_memo           | 39.7 us                                                    | 39.3 us: 1.01x faster                                                   |
| sqlglot_parse           | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                   |
| json_loads              | 28.9 us                                                    | 28.6 us: 1.01x faster                                                   |
| tornado_http            | 94.6 ms                                                    | 93.8 ms: 1.01x faster                                                   |
| sympy_sum               | 156 ms                                                     | 154 ms: 1.01x faster                                                    |
| fannkuch                | 402 ms                                                     | 398 ms: 1.01x faster                                                    |
| unpickle_pure_python    | 218 us                                                     | 216 us: 1.01x faster                                                    |
| sqlglot_normalize       | 110 ms                                                     | 109 ms: 1.01x faster                                                    |
| unpickle_list           | 5.34 us                                                    | 5.31 us: 1.01x faster                                                   |
| mako                    | 11.2 ms                                                    | 11.2 ms: 1.01x faster                                                   |
| pidigits                | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.83 sec: 1.01x faster                                                  |
| comprehensions          | 16.6 us                                                    | 16.5 us: 1.00x faster                                                   |
| python_startup_no_site  | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                   |
| logging_silent          | 105 ns                                                     | 105 ns: 1.01x slower                                                    |
| json                    | 5.31 ms                                                    | 5.36 ms: 1.01x slower                                                   |
| deltablue               | 3.25 ms                                                    | 3.29 ms: 1.01x slower                                                   |
| pickle_dict             | 34.8 us                                                    | 35.2 us: 1.01x slower                                                   |
| tomli_loads             | 2.12 sec                                                   | 2.15 sec: 1.01x slower                                                  |
| pickle_list             | 5.11 us                                                    | 5.18 us: 1.02x slower                                                   |
| pickle                  | 11.5 us                                                    | 11.8 us: 1.03x slower                                                   |
| async_tree_cpu_io_mixed | 611 ms                                                     | 631 ms: 1.03x slower                                                    |
| pycparser               | 1.16 sec                                                   | 1.20 sec: 1.03x slower                                                  |
| regex_effbot            | 3.67 ms                                                    | 3.80 ms: 1.03x slower                                                   |
| regex_v8                | 25.1 ms                                                    | 26.0 ms: 1.04x slower                                                   |
| regex_dna               | 221 ms                                                     | 233 ms: 1.06x slower                                                    |
| Geometric mean          | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (20): async_tree_io_tg, async_tree_memoization_tg, async_tree_none, pylint, telco, typing_runtime_protocols, sympy_expand, coroutines, async_generators, bench_mp_pool, bench_thread_pool, dask, gc_traversal, asyncio_websockets, async_tree_none_tg, unpickle, html5lib, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x