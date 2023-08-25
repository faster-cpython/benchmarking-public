
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                   |
| docutils       | 2.63 sec                                               | 2.56 sec: 1.02x faster                                 |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.1 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.4 ms: 1.07x faster                                  |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| float          | 77.2 ms                                                | 75.2 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                  |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.43 ms: 1.33x faster                                  |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                   |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                   |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                   |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                  |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                   |
| pickle_list          | 4.11 us                                                | 4.20 us: 1.02x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.07 us: 1.03x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 56.0 ms: 1.04x slower                                  |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.9 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.83 ms: 1.04x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.8 ms: 1.08x faster                                  |
| genshi_text     | 21.6 ms                                                | 21.3 ms: 1.01x faster                                  |
| mako            | 10.1 ms                                                | 10.1 ms: 1.01x slower                                  |
| django_template | 32.6 ms                                                | 33.8 ms: 1.04x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.46x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 505 ms: 1.82x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.43 ms: 1.33x faster                                  |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                   |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| gc_traversal            | 4.02 ms                                                | 3.60 ms: 1.12x faster                                  |
| coroutines              | 25.5 ms                                                | 22.9 ms: 1.11x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                  |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.09x faster                                  |
| genshi_xml              | 51.8 ms                                                | 47.8 ms: 1.08x faster                                  |
| json                    | 4.94 ms                                                | 4.62 ms: 1.07x faster                                  |
| nbody                   | 93.1 ms                                                | 87.4 ms: 1.07x faster                                  |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                 |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                   |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                   |
| tornado_http            | 96.3 ms                                                | 91.1 ms: 1.06x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 35.1 us: 1.05x faster                                  |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| html5lib                | 64.5 ms                                                | 61.4 ms: 1.05x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.29 ms: 1.05x faster                                  |
| coverage                | 100 ms                                                 | 95.5 ms: 1.05x faster                                  |
| scimark_fft             | 328 ms                                                 | 314 ms: 1.05x faster                                   |
| logging_silent          | 101 ns                                                 | 96.6 ns: 1.05x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.10 ms: 1.04x faster                                  |
| chaos                   | 69.2 ms                                                | 66.2 ms: 1.04x faster                                  |
| bench_thread_pool       | 819 us                                                 | 786 us: 1.04x faster                                   |
| logging_format          | 6.68 us                                                | 6.42 us: 1.04x faster                                  |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 51.2 ms: 1.04x faster                                  |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                   |
| spectral_norm           | 100 ms                                                 | 96.5 ms: 1.04x faster                                  |
| raytrace                | 297 ms                                                 | 286 ms: 1.04x faster                                   |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.04x faster                                 |
| richards                | 45.7 ms                                                | 44.3 ms: 1.03x faster                                  |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                   |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                   |
| scimark_sor             | 118 ms                                                 | 115 ms: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                   |
| float                   | 77.2 ms                                                | 75.2 ms: 1.03x faster                                  |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                  |
| nqueens                 | 83.4 ms                                                | 81.3 ms: 1.03x faster                                  |
| docutils                | 2.63 sec                                               | 2.56 sec: 1.02x faster                                 |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                 |
| sympy_str               | 290 ms                                                 | 283 ms: 1.02x faster                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.6 ms: 1.02x faster                                  |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.01x faster                                   |
| crypto_pyaes            | 74.7 ms                                                | 73.8 ms: 1.01x faster                                  |
| telco                   | 6.58 ms                                                | 6.51 ms: 1.01x faster                                  |
| genshi_text             | 21.6 ms                                                | 21.3 ms: 1.01x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 694 ms: 1.01x faster                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                   |
| fannkuch                | 388 ms                                                 | 385 ms: 1.01x faster                                   |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                  |
| dulwich_log             | 63.7 ms                                                | 63.4 ms: 1.00x faster                                  |
| pyflate                 | 418 ms                                                 | 420 ms: 1.01x slower                                   |
| mako                    | 10.1 ms                                                | 10.1 ms: 1.01x slower                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.02x slower                                  |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                   |
| pickle_list             | 4.11 us                                                | 4.20 us: 1.02x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.00 us: 1.02x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.07 us: 1.03x slower                                  |
| thrift                  | 756 us                                                 | 783 us: 1.04x slower                                   |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.04x slower                                  |
| python_startup          | 8.52 ms                                                | 8.83 ms: 1.04x slower                                  |
| django_template         | 32.6 ms                                                | 33.8 ms: 1.04x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 56.0 ms: 1.04x slower                                  |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 657 ms: 1.05x slower                                   |
| xml_etree_generate      | 76.2 ms                                                | 80.9 ms: 1.06x slower                                  |
| comprehensions          | 22.4 us                                                | 23.9 us: 1.06x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 46.4 ns: 1.08x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                  |
| async_generators        | 368 ms                                                 | 411 ms: 1.12x slower                                   |
| dask                    | 360 ms                                                 | 512 ms: 1.42x slower                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (11): scimark_lu, async_tree_none, async_tree_io, bench_mp_pool, sympy_sum, create_gc_cycles, djangocms, go, async_tree_cpu_io_mixed, chameleon, scimark_monte_carlo
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
