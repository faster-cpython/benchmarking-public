# Results vs. 3.13.0b2

- fork: python
- ref: ac37a806018cc40fafeb
- machine: linux-x86_64
- commit hash: ac37a80
- commit date: 2024-06-17
- overall geometric mean: 1.02x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                |
| tornado_http   | 94.6 ms                                                    | 93.8 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|-------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 630 ms: 1.03x slower                                                  |
| async_tree_io           | 939 ms                                                     | 976 ms: 1.04x slower                                                  |
| Geometric mean          | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                 |
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                 |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                                  |
| regex_v8       | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|--------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process  | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                 |
| xml_etree_generate | 87.4 ms                                                    | 85.8 ms: 1.02x faster                                                 |
| json_dumps         | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                 |
| pickle_list        | 5.11 us                                                    | 5.05 us: 1.01x faster                                                 |
| json_loads         | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| tomli_loads        | 2.12 sec                                                   | 2.11 sec: 1.01x faster                                                |
| pickle_dict        | 34.8 us                                                    | 34.7 us: 1.00x faster                                                 |
| pickle_pure_python | 305 us                                                     | 307 us: 1.01x slower                                                  |
| unpickle_list      | 5.34 us                                                    | 5.49 us: 1.03x slower                                                 |
| pickle             | 11.5 us                                                    | 11.8 us: 1.03x slower                                                 |
| Geometric mean     | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, unpickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                                 |
| mako            | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|-------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                | 367 us                                                     | 266 us: 1.38x faster                                                  |
| deepcopy_memo           | 39.7 us                                                    | 29.7 us: 1.34x faster                                                 |
| deepcopy_reduce         | 3.35 us                                                    | 2.69 us: 1.24x faster                                                 |
| gc_traversal            | 3.98 ms                                                    | 3.57 ms: 1.12x faster                                                 |
| pathlib                 | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                 |
| scimark_fft             | 392 ms                                                     | 372 ms: 1.06x faster                                                  |
| richards_super          | 57.4 ms                                                    | 55.1 ms: 1.04x faster                                                 |
| asyncio_tcp             | 508 ms                                                     | 488 ms: 1.04x faster                                                  |
| create_gc_cycles        | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                 |
| crypto_pyaes            | 77.5 ms                                                    | 74.5 ms: 1.04x faster                                                 |
| richards                | 50.9 ms                                                    | 49.0 ms: 1.04x faster                                                 |
| thrift                  | 823 us                                                     | 796 us: 1.03x faster                                                  |
| fannkuch                | 402 ms                                                     | 389 ms: 1.03x faster                                                  |
| regex_compile           | 137 ms                                                     | 133 ms: 1.03x faster                                                  |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 5.13 ms: 1.03x faster                                                 |
| scimark_lu              | 122 ms                                                     | 118 ms: 1.03x faster                                                  |
| coroutines              | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                                 |
| dulwich_log             | 67.2 ms                                                    | 65.5 ms: 1.03x faster                                                 |
| logging_format          | 6.47 us                                                    | 6.31 us: 1.03x faster                                                 |
| nqueens                 | 81.4 ms                                                    | 79.5 ms: 1.02x faster                                                 |
| hexiom                  | 6.30 ms                                                    | 6.16 ms: 1.02x faster                                                 |
| xml_etree_process       | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                 |
| logging_silent          | 105 ns                                                     | 103 ns: 1.02x faster                                                  |
| xml_etree_generate      | 87.4 ms                                                    | 85.8 ms: 1.02x faster                                                 |
| spectral_norm           | 116 ms                                                     | 114 ms: 1.02x faster                                                  |
| docutils                | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                |
| generators              | 29.6 ms                                                    | 29.2 ms: 1.01x faster                                                 |
| sqlglot_optimize        | 55.5 ms                                                    | 54.8 ms: 1.01x faster                                                 |
| json_dumps              | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                 |
| logging_simple          | 5.74 us                                                    | 5.67 us: 1.01x faster                                                 |
| django_template         | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                                 |
| 2to3                    | 274 ms                                                     | 271 ms: 1.01x faster                                                  |
| meteor_contest          | 110 ms                                                     | 109 ms: 1.01x faster                                                  |
| sympy_str               | 282 ms                                                     | 279 ms: 1.01x faster                                                  |
| pickle_list             | 5.11 us                                                    | 5.05 us: 1.01x faster                                                 |
| sqlite_synth            | 2.99 us                                                    | 2.96 us: 1.01x faster                                                 |
| float                   | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                 |
| json_loads              | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| mdp                     | 2.79 sec                                                   | 2.76 sec: 1.01x faster                                                |
| sympy_integrate         | 20.5 ms                                                    | 20.3 ms: 1.01x faster                                                 |
| tornado_http            | 94.6 ms                                                    | 93.8 ms: 1.01x faster                                                 |
| pidigits                | 191 ms                                                     | 190 ms: 1.01x faster                                                  |
| pprint_safe_repr        | 758 ms                                                     | 752 ms: 1.01x faster                                                  |
| chaos                   | 61.3 ms                                                    | 60.9 ms: 1.01x faster                                                 |
| sqlglot_transpile       | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                 |
| pprint_pformat          | 1.56 sec                                                   | 1.55 sec: 1.01x faster                                                |
| python_startup          | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.83 sec: 1.01x faster                                                |
| tomli_loads             | 2.12 sec                                                   | 2.11 sec: 1.01x faster                                                |
| pickle_dict             | 34.8 us                                                    | 34.7 us: 1.00x faster                                                 |
| python_startup_no_site  | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                 |
| pickle_pure_python      | 305 us                                                     | 307 us: 1.01x slower                                                  |
| sqlglot_parse           | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                 |
| go                      | 145 ms                                                     | 146 ms: 1.01x slower                                                  |
| async_generators        | 442 ms                                                     | 446 ms: 1.01x slower                                                  |
| json                    | 5.31 ms                                                    | 5.39 ms: 1.02x slower                                                 |
| pyflate                 | 484 ms                                                     | 492 ms: 1.02x slower                                                  |
| mako                    | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                                 |
| regex_effbot            | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                 |
| regex_dna               | 221 ms                                                     | 227 ms: 1.03x slower                                                  |
| comprehensions          | 16.6 us                                                    | 17.1 us: 1.03x slower                                                 |
| unpickle_list           | 5.34 us                                                    | 5.49 us: 1.03x slower                                                 |
| async_tree_cpu_io_mixed | 611 ms                                                     | 630 ms: 1.03x slower                                                  |
| pickle                  | 11.5 us                                                    | 11.8 us: 1.03x slower                                                 |
| pycparser               | 1.16 sec                                                   | 1.20 sec: 1.03x slower                                                |
| async_tree_io           | 939 ms                                                     | 976 ms: 1.04x slower                                                  |
| regex_v8                | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                 |
| scimark_sor             | 127 ms                                                     | 135 ms: 1.06x slower                                                  |
| Geometric mean          | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (29): xml_etree_parse, async_tree_none, async_tree_memoization_tg, dask, async_tree_io_tg, genshi_text, bpe_tokeniser, typing_runtime_protocols, genshi_xml, sympy_expand, scimark_monte_carlo, telco, sqlglot_normalize, pylint, xml_etree_iterparse, raytrace, unpickle, sympy_sum, asyncio_websockets, bench_mp_pool, nbody, bench_thread_pool, deltablue, html5lib, coverage, unpickle_pure_python, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x