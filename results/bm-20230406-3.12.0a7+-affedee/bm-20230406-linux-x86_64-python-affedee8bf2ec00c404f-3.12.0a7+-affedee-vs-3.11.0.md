
# Results vs. 3.11.0

- fork: python
- ref: affedee8bf2ec00c404f
- machine: linux-x86_64
- commit hash: affedee
- commit date: 2023-04-06
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.27 ms: 1.03x faster                                                  |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                 |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                  |
| tornado_http   | 96.3 ms                                                | 90.8 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 86.9 ms: 1.07x faster                                                  |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                   |
| float          | 77.2 ms                                                | 73.5 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.48 ms: 1.15x faster                                                  |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                   |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.47 ms: 1.33x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 203 us: 1.13x faster                                                   |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 146 ms: 1.09x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 289 us: 1.06x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 99.3 ms: 1.05x faster                                                  |
| xml_etree_process    | 53.9 ms                                                | 55.2 ms: 1.02x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.11 us: 1.04x slower                                                  |
| pickle_dict          | 31.1 us                                                | 32.6 us: 1.05x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.35 us: 1.06x slower                                                  |
| pickle               | 10.1 us                                                | 10.7 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.81 ms: 1.03x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| mako           | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                  |
| genshi_text    | 21.6 ms                                                | 21.9 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.1 ms: 2.53x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.47 ms: 1.33x faster                                                  |
| mypy2                   | 420 ms                                                 | 336 ms: 1.25x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.48 ms: 1.15x faster                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.22 ms: 1.15x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.51 ms: 1.13x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 203 us: 1.13x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| gc_traversal            | 4.02 ms                                                | 3.65 ms: 1.10x faster                                                  |
| spectral_norm           | 100 ms                                                 | 91.3 ms: 1.10x faster                                                  |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 33.9 us: 1.09x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 146 ms: 1.09x faster                                                   |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.08x faster                                                  |
| coroutines              | 25.5 ms                                                | 23.6 ms: 1.08x faster                                                  |
| json                    | 4.94 ms                                                | 4.58 ms: 1.08x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                  |
| nbody                   | 93.1 ms                                                | 86.9 ms: 1.07x faster                                                  |
| scimark_sor             | 118 ms                                                 | 110 ms: 1.07x faster                                                   |
| logging_silent          | 101 ns                                                 | 94.9 ns: 1.07x faster                                                  |
| hexiom                  | 6.37 ms                                                | 5.99 ms: 1.06x faster                                                  |
| tornado_http            | 96.3 ms                                                | 90.8 ms: 1.06x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 289 us: 1.06x faster                                                   |
| deepcopy                | 342 us                                                 | 324 us: 1.06x faster                                                   |
| logging_format          | 6.68 us                                                | 6.33 us: 1.06x faster                                                  |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                   |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                                  |
| float                   | 77.2 ms                                                | 73.5 ms: 1.05x faster                                                  |
| html5lib                | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                  |
| comprehensions          | 22.4 us                                                | 21.4 us: 1.05x faster                                                  |
| nqueens                 | 83.4 ms                                                | 79.6 ms: 1.05x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 99.3 ms: 1.05x faster                                                  |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.05x faster                                                   |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 50.9 ms: 1.04x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                                 |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                   |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                   |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                 |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                 |
| fannkuch                | 388 ms                                                 | 374 ms: 1.04x faster                                                   |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.34 ms: 1.04x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| crypto_pyaes            | 74.7 ms                                                | 72.2 ms: 1.03x faster                                                  |
| chaos                   | 69.2 ms                                                | 66.9 ms: 1.03x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                  |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| chameleon               | 6.47 ms                                                | 6.27 ms: 1.03x faster                                                  |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| richards                | 45.7 ms                                                | 44.4 ms: 1.03x faster                                                  |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                   |
| pprint_safe_repr        | 701 ms                                                 | 685 ms: 1.02x faster                                                   |
| telco                   | 6.58 ms                                                | 6.44 ms: 1.02x faster                                                  |
| mako                    | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                 |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 66.8 ms: 1.02x faster                                                  |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.6 ms: 1.02x faster                                                  |
| coverage                | 100 ms                                                 | 98.7 ms: 1.01x faster                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                   |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                   |
| dulwich_log             | 63.7 ms                                                | 63.3 ms: 1.01x faster                                                  |
| pyflate                 | 418 ms                                                 | 422 ms: 1.01x slower                                                   |
| genshi_text             | 21.6 ms                                                | 21.9 ms: 1.02x slower                                                  |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 55.2 ms: 1.02x slower                                                  |
| python_startup          | 8.52 ms                                                | 8.81 ms: 1.03x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 44.6 ns: 1.03x slower                                                  |
| unpickle_list           | 4.91 us                                                | 5.11 us: 1.04x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.64 us: 1.05x slower                                                  |
| pickle_dict             | 31.1 us                                                | 32.6 us: 1.05x slower                                                  |
| thrift                  | 756 us                                                 | 800 us: 1.06x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.35 us: 1.06x slower                                                  |
| pickle                  | 10.1 us                                                | 10.7 us: 1.07x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                  |
| async_generators        | 368 ms                                                 | 414 ms: 1.12x slower                                                   |
| dask                    | 360 ms                                                 | 502 ms: 1.39x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (11): djangocms, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, unpickle, bench_mp_pool, regex_dna, deepcopy_reduce, django_template, pathlib, async_tree_memoization
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
