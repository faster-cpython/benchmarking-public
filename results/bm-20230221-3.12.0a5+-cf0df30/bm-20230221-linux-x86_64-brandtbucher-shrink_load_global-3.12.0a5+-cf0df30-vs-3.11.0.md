
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: cf0df30
- commit date: 2023-02-21
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                                       |
| chameleon      | 6.47 ms                                                | 6.38 ms: 1.02x faster                                                      |
| docutils       | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                     |
| html5lib       | 64.5 ms                                                | 61.0 ms: 1.06x faster                                                      |
| tornado_http   | 96.3 ms                                                | 94.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.3 ms: 1.07x faster                                                      |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                       |
| nbody          | 93.1 ms                                                | 94.2 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                      |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                       |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                                       |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                       |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| unpickle             | 13.7 us                                                | 13.1 us: 1.05x faster                                                      |
| pickle_dict          | 31.1 us                                                | 30.4 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| pickle_list          | 4.11 us                                                | 4.13 us: 1.00x slower                                                      |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                      |
| xml_etree_process    | 53.9 ms                                                | 54.5 ms: 1.01x slower                                                      |
| unpickle_list        | 4.91 us                                                | 5.03 us: 1.03x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 80.0 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.01 ms: 1.06x slower                                                      |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                      |
| genshi_text     | 21.6 ms                                                | 20.6 ms: 1.05x faster                                                      |
| mako            | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                      |
| django_template | 32.6 ms                                                | 33.3 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.46x faster                                                      |
| asyncio_tcp             | 922 ms                                                 | 502 ms: 1.84x faster                                                       |
| json_dumps              | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                      |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.13 ms: 1.17x faster                                                      |
| coroutines              | 25.5 ms                                                | 21.9 ms: 1.16x faster                                                      |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                       |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.03 ms: 1.12x faster                                                      |
| gc_traversal            | 4.02 ms                                                | 3.61 ms: 1.11x faster                                                      |
| genshi_xml              | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                      |
| logging_silent          | 101 ns                                                 | 91.0 ns: 1.11x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                      |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                      |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                                      |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                      |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                                       |
| fannkuch                | 388 ms                                                 | 359 ms: 1.08x faster                                                       |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                       |
| json                    | 4.94 ms                                                | 4.58 ms: 1.08x faster                                                      |
| nqueens                 | 83.4 ms                                                | 77.5 ms: 1.08x faster                                                      |
| richards                | 45.7 ms                                                | 42.6 ms: 1.07x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| float                   | 77.2 ms                                                | 72.3 ms: 1.07x faster                                                      |
| logging_format          | 6.68 us                                                | 6.26 us: 1.07x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                                     |
| spectral_norm           | 100 ms                                                 | 94.5 ms: 1.06x faster                                                      |
| html5lib                | 64.5 ms                                                | 61.0 ms: 1.06x faster                                                      |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                     |
| hexiom                  | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                      |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                       |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 35.2 us: 1.05x faster                                                      |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.75 us: 1.05x faster                                                      |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.05x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 50.7 ms: 1.05x faster                                                      |
| unpickle                | 13.7 us                                                | 13.1 us: 1.05x faster                                                      |
| chaos                   | 69.2 ms                                                | 66.2 ms: 1.04x faster                                                      |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                                       |
| pyflate                 | 418 ms                                                 | 401 ms: 1.04x faster                                                       |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 675 ms: 1.04x faster                                                       |
| bench_thread_pool       | 819 us                                                 | 788 us: 1.04x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                      |
| crypto_pyaes            | 74.7 ms                                                | 72.3 ms: 1.03x faster                                                      |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                                       |
| coverage                | 100 ms                                                 | 97.2 ms: 1.03x faster                                                      |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                                       |
| async_tree_memoization  | 627 ms                                                 | 610 ms: 1.03x faster                                                       |
| telco                   | 6.58 ms                                                | 6.42 ms: 1.03x faster                                                      |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                                       |
| pickle_dict             | 31.1 us                                                | 30.4 us: 1.02x faster                                                      |
| tornado_http            | 96.3 ms                                                | 94.5 ms: 1.02x faster                                                      |
| scimark_monte_carlo     | 68.1 ms                                                | 66.9 ms: 1.02x faster                                                      |
| chameleon               | 6.47 ms                                                | 6.38 ms: 1.02x faster                                                      |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                      |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                                       |
| docutils                | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                     |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                                      |
| mako                    | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                      |
| sympy_sum               | 167 ms                                                 | 166 ms: 1.01x faster                                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.49 ms: 1.00x slower                                                      |
| pickle_list             | 4.11 us                                                | 4.13 us: 1.00x slower                                                      |
| thrift                  | 756 us                                                 | 760 us: 1.01x slower                                                       |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                      |
| nbody                   | 93.1 ms                                                | 94.2 ms: 1.01x slower                                                      |
| xml_etree_process       | 53.9 ms                                                | 54.5 ms: 1.01x slower                                                      |
| deepcopy_reduce         | 2.94 us                                                | 2.98 us: 1.01x slower                                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.01x slower                                                      |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                      |
| django_template         | 32.6 ms                                                | 33.3 ms: 1.02x slower                                                      |
| unpickle_list           | 4.91 us                                                | 5.03 us: 1.03x slower                                                      |
| unpack_sequence         | 43.1 ns                                                | 44.7 ns: 1.04x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 80.0 ms: 1.05x slower                                                      |
| python_startup          | 8.52 ms                                                | 9.01 ms: 1.06x slower                                                      |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                      |
| async_generators        | 368 ms                                                 | 407 ms: 1.11x slower                                                       |
| dask                    | 360 ms                                                 | 497 ms: 1.38x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, bench_mp_pool, async_tree_io, sqlalchemy_imperative, sqlalchemy_declarative, sqlglot_transpile, djangocms
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
