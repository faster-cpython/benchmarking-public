
# Results vs. 3.11.0

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: linux-x86_64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.05x faster                                                  |
| chameleon      | 6.47 ms                                                | 6.45 ms: 1.00x faster                                                 |
| docutils       | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.2 ms: 1.06x faster                                                 |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                 |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                  |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                 |
| regex_dna      | 204 ms                                                 | 217 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.52 ms: 1.32x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                                  |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                                 |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                  |
| pickle_list          | 4.11 us                                                | 3.95 us: 1.04x faster                                                 |
| unpickle             | 13.7 us                                                | 13.3 us: 1.02x faster                                                 |
| xml_etree_generate   | 76.2 ms                                                | 76.9 ms: 1.01x slower                                                 |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                                 |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 6.07 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                 |
| mako            | 10.1 ms                                                | 9.43 ms: 1.07x faster                                                 |
| genshi_text     | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                 |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.52 ms: 1.32x faster                                                 |
| mypy2                   | 420 ms                                                 | 329 ms: 1.28x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                 |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                                  |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.13x faster                                                  |
| logging_silent          | 101 ns                                                 | 90.9 ns: 1.11x faster                                                 |
| json_loads              | 26.5 us                                                | 23.8 us: 1.11x faster                                                 |
| regex_effbot            | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                 |
| richards                | 45.7 ms                                                | 42.0 ms: 1.09x faster                                                 |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                                  |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                 |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                                 |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                                |
| genshi_xml              | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.20 ms: 1.07x faster                                                 |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                  |
| mako                    | 10.1 ms                                                | 9.43 ms: 1.07x faster                                                 |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                  |
| json                    | 4.94 ms                                                | 4.67 ms: 1.06x faster                                                 |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                                  |
| float                   | 77.2 ms                                                | 73.2 ms: 1.06x faster                                                 |
| gc_traversal            | 4.02 ms                                                | 3.81 ms: 1.05x faster                                                 |
| 2to3                    | 259 ms                                                 | 246 ms: 1.05x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 778 us: 1.05x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.6 ms: 1.05x faster                                                 |
| hexiom                  | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                 |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                                |
| scimark_fft             | 328 ms                                                 | 314 ms: 1.05x faster                                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.63 ms: 1.04x faster                                                 |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.04x faster                                                 |
| logging_format          | 6.68 us                                                | 6.41 us: 1.04x faster                                                 |
| spectral_norm           | 100 ms                                                 | 96.0 ms: 1.04x faster                                                 |
| pickle_list             | 4.11 us                                                | 3.95 us: 1.04x faster                                                 |
| nqueens                 | 83.4 ms                                                | 80.1 ms: 1.04x faster                                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 65.4 ms: 1.04x faster                                                 |
| async_generators        | 368 ms                                                 | 354 ms: 1.04x faster                                                  |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 890 ms: 1.04x faster                                                  |
| chaos                   | 69.2 ms                                                | 66.9 ms: 1.03x faster                                                 |
| create_gc_cycles        | 1.49 ms                                                | 1.44 ms: 1.03x faster                                                 |
| genshi_text             | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                 |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                  |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.03x faster                                                  |
| pyflate                 | 418 ms                                                 | 405 ms: 1.03x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                 |
| logging_simple          | 6.03 us                                                | 5.88 us: 1.03x faster                                                 |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| sympy_str               | 290 ms                                                 | 283 ms: 1.02x faster                                                  |
| fannkuch                | 388 ms                                                 | 379 ms: 1.02x faster                                                  |
| unpickle                | 13.7 us                                                | 13.3 us: 1.02x faster                                                 |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                                  |
| docutils                | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                |
| coroutines              | 25.5 ms                                                | 25.0 ms: 1.02x faster                                                 |
| telco                   | 6.58 ms                                                | 6.46 ms: 1.02x faster                                                 |
| dulwich_log             | 63.7 ms                                                | 62.5 ms: 1.02x faster                                                 |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.01x faster                                                  |
| thrift                  | 756 us                                                 | 751 us: 1.01x faster                                                  |
| chameleon               | 6.47 ms                                                | 6.45 ms: 1.00x faster                                                 |
| crypto_pyaes            | 74.7 ms                                                | 75.3 ms: 1.01x slower                                                 |
| xml_etree_generate      | 76.2 ms                                                | 76.9 ms: 1.01x slower                                                 |
| deepcopy_reduce         | 2.94 us                                                | 2.97 us: 1.01x slower                                                 |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                 |
| python_startup_no_site  | 6.01 ms                                                | 6.07 ms: 1.01x slower                                                 |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                                 |
| regex_v8                | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                 |
| pickle_dict             | 31.1 us                                                | 31.5 us: 1.01x slower                                                 |
| async_tree_none         | 526 ms                                                 | 536 ms: 1.02x slower                                                  |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                 |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                                |
| async_tree_cpu_io_mixed | 739 ms                                                 | 769 ms: 1.04x slower                                                  |
| comprehensions          | 22.4 us                                                | 23.5 us: 1.05x slower                                                 |
| async_tree_memoization  | 627 ms                                                 | 665 ms: 1.06x slower                                                  |
| regex_dna               | 204 ms                                                 | 217 ms: 1.06x slower                                                  |
| generators              | 73.5 ms                                                | 79.1 ms: 1.08x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (10): xml_etree_process, python_startup, bench_mp_pool, unpack_sequence, dask, pathlib, xml_etree_iterparse, djangocms, pickle, nbody
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
