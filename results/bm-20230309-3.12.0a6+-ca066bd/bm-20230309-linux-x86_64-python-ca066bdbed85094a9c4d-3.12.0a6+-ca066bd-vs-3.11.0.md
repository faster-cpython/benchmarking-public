
# Results vs. 3.11.0

- fork: python
- ref: ca066bdbed85094a9c4d
- machine: linux-x86_64
- commit hash: ca066bd
- commit date: 2023-03-09
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                  |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                 |
| html5lib       | 64.5 ms                                                | 62.1 ms: 1.04x faster                                                  |
| tornado_http   | 96.3 ms                                                | 95.1 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| float          | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.56 ms: 1.12x faster                                                  |
| regex_compile  | 138 ms                                                 | 135 ms: 1.03x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                  |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 204 us: 1.12x faster                                                   |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                                   |
| unpickle             | 13.7 us                                                | 13.2 us: 1.03x faster                                                  |
| pickle_dict          | 31.1 us                                                | 31.0 us: 1.01x faster                                                  |
| pickle_list          | 4.11 us                                                | 4.16 us: 1.01x slower                                                  |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                  |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.01 ms: 1.06x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                  |
| mako            | 10.1 ms                                                | 9.95 ms: 1.01x faster                                                  |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                  |
| mypy2                   | 420 ms                                                 | 335 ms: 1.26x faster                                                   |
| gc_traversal            | 4.02 ms                                                | 3.55 ms: 1.13x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.56 ms: 1.12x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.27 ms: 1.12x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 204 us: 1.12x faster                                                   |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.10x faster                                                   |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                  |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                  |
| coroutines              | 25.5 ms                                                | 23.5 ms: 1.08x faster                                                  |
| fannkuch                | 388 ms                                                 | 359 ms: 1.08x faster                                                   |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                  |
| logging_silent          | 101 ns                                                 | 93.6 ns: 1.08x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                   |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                                   |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                                  |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                                   |
| spectral_norm           | 100 ms                                                 | 94.3 ms: 1.06x faster                                                  |
| coverage                | 100 ms                                                 | 94.5 ms: 1.06x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 35.0 us: 1.06x faster                                                  |
| richards                | 45.7 ms                                                | 43.6 ms: 1.05x faster                                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                 |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                 |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                                  |
| float                   | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                  |
| html5lib                | 64.5 ms                                                | 62.1 ms: 1.04x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| nqueens                 | 83.4 ms                                                | 80.2 ms: 1.04x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 791 us: 1.03x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                                   |
| unpickle                | 13.7 us                                                | 13.2 us: 1.03x faster                                                  |
| raytrace                | 297 ms                                                 | 288 ms: 1.03x faster                                                   |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                 |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                                   |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                   |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                                 |
| regex_compile           | 138 ms                                                 | 135 ms: 1.03x faster                                                   |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                                   |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                  |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| logging_format          | 6.68 us                                                | 6.56 us: 1.02x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.6 ms: 1.02x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.26 ms: 1.02x faster                                                  |
| chameleon               | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                  |
| deepcopy                | 342 us                                                 | 337 us: 1.01x faster                                                   |
| mako                    | 10.1 ms                                                | 9.95 ms: 1.01x faster                                                  |
| telco                   | 6.58 ms                                                | 6.50 ms: 1.01x faster                                                  |
| tornado_http            | 96.3 ms                                                | 95.1 ms: 1.01x faster                                                  |
| logging_simple          | 6.03 us                                                | 5.96 us: 1.01x faster                                                  |
| sympy_str               | 290 ms                                                 | 287 ms: 1.01x faster                                                   |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                  |
| chaos                   | 69.2 ms                                                | 68.7 ms: 1.01x faster                                                  |
| crypto_pyaes            | 74.7 ms                                                | 74.2 ms: 1.01x faster                                                  |
| pickle_dict             | 31.1 us                                                | 31.0 us: 1.01x faster                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.00x faster                                                  |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                                   |
| pickle_list             | 4.11 us                                                | 4.16 us: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.55 ms: 1.01x slower                                                  |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                                  |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.02x slower                                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.01 us: 1.03x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                                  |
| scimark_lu              | 110 ms                                                 | 113 ms: 1.03x slower                                                   |
| thrift                  | 756 us                                                 | 778 us: 1.03x slower                                                   |
| xml_etree_process       | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                  |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                                  |
| async_tree_memoization  | 627 ms                                                 | 657 ms: 1.05x slower                                                   |
| python_startup          | 8.52 ms                                                | 9.01 ms: 1.06x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                  |
| comprehensions          | 22.4 us                                                | 23.9 us: 1.07x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                  |
| async_generators        | 368 ms                                                 | 413 ms: 1.12x slower                                                   |
| dask                    | 360 ms                                                 | 509 ms: 1.41x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (14): async_tree_none, genshi_text, go, djangocms, unpack_sequence, nbody, bench_mp_pool, async_tree_io, dulwich_log, sympy_sum, async_tree_cpu_io_mixed, sqlalchemy_declarative, scimark_monte_carlo, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
