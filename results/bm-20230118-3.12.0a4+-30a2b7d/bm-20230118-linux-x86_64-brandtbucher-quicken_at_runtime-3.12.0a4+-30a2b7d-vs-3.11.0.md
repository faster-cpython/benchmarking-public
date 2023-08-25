
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 30a2b7d
- commit date: 2023-01-18
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.03x faster                                                       |
| chameleon      | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                      |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| html5lib       | 64.5 ms                                                | 60.5 ms: 1.07x faster                                                      |
| tornado_http   | 96.3 ms                                                | 94.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.8 ms: 1.08x faster                                                      |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.68 ms: 1.09x faster                                                      |
| regex_compile  | 138 ms                                                 | 127 ms: 1.08x faster                                                       |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                      |
| regex_dna      | 204 ms                                                 | 216 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.43 ms: 1.33x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.14x faster                                                       |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                       |
| unpickle             | 13.7 us                                                | 13.2 us: 1.03x faster                                                      |
| xml_etree_process    | 53.9 ms                                                | 54.2 ms: 1.01x slower                                                      |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 78.2 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (3): pickle_list, pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.71 ms: 1.02x slower                                                      |
| python_startup_no_site | 6.01 ms                                                | 6.25 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                      |
| genshi_text     | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                      |
| mako            | 10.1 ms                                                | 9.78 ms: 1.03x faster                                                      |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 495 ms: 1.86x faster                                                       |
| json_dumps              | 12.6 ms                                                | 9.43 ms: 1.33x faster                                                      |
| deltablue               | 3.67 ms                                                | 3.17 ms: 1.16x faster                                                      |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.14x faster                                                       |
| logging_silent          | 101 ns                                                 | 90.1 ns: 1.12x faster                                                      |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.02 ms: 1.12x faster                                                      |
| aiohttp                 | 1.10 ms                                                | 993 us: 1.11x faster                                                       |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                      |
| chaos                   | 69.2 ms                                                | 62.8 ms: 1.10x faster                                                      |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                      |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.10x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 33.8 us: 1.09x faster                                                      |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.68 ms: 1.09x faster                                                      |
| hexiom                  | 6.37 ms                                                | 5.87 ms: 1.09x faster                                                      |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                                       |
| fannkuch                | 388 ms                                                 | 357 ms: 1.08x faster                                                       |
| nqueens                 | 83.4 ms                                                | 76.9 ms: 1.08x faster                                                      |
| regex_compile           | 138 ms                                                 | 127 ms: 1.08x faster                                                       |
| scimark_fft             | 328 ms                                                 | 304 ms: 1.08x faster                                                       |
| sympy_str               | 290 ms                                                 | 269 ms: 1.08x faster                                                       |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.08x faster                                                       |
| float                   | 77.2 ms                                                | 71.8 ms: 1.08x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 19.6 ms: 1.07x faster                                                      |
| html5lib                | 64.5 ms                                                | 60.5 ms: 1.07x faster                                                      |
| json                    | 4.94 ms                                                | 4.64 ms: 1.07x faster                                                      |
| raytrace                | 297 ms                                                 | 279 ms: 1.06x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                                       |
| pyflate                 | 418 ms                                                 | 396 ms: 1.06x faster                                                       |
| deepcopy                | 342 us                                                 | 324 us: 1.05x faster                                                       |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                     |
| async_generators        | 368 ms                                                 | 350 ms: 1.05x faster                                                       |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 780 us: 1.05x faster                                                       |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.49 sec: 1.05x faster                                                     |
| richards                | 45.7 ms                                                | 43.7 ms: 1.05x faster                                                      |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.04x faster                                                      |
| logging_format          | 6.68 us                                                | 6.40 us: 1.04x faster                                                      |
| telco                   | 6.58 ms                                                | 6.32 ms: 1.04x faster                                                      |
| logging_simple          | 6.03 us                                                | 5.80 us: 1.04x faster                                                      |
| scimark_monte_carlo     | 68.1 ms                                                | 65.5 ms: 1.04x faster                                                      |
| pprint_safe_repr        | 701 ms                                                 | 676 ms: 1.04x faster                                                       |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                      |
| 2to3                    | 259 ms                                                 | 250 ms: 1.03x faster                                                       |
| unpickle                | 13.7 us                                                | 13.2 us: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                       |
| mako                    | 10.1 ms                                                | 9.78 ms: 1.03x faster                                                      |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                     |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                       |
| coroutines              | 25.5 ms                                                | 24.8 ms: 1.03x faster                                                      |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                      |
| crypto_pyaes            | 74.7 ms                                                | 73.3 ms: 1.02x faster                                                      |
| tornado_http            | 96.3 ms                                                | 94.9 ms: 1.01x faster                                                      |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                      |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                                      |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                      |
| thrift                  | 756 us                                                 | 752 us: 1.01x faster                                                       |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                       |
| chameleon               | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                      |
| xml_etree_process       | 53.9 ms                                                | 54.2 ms: 1.01x slower                                                      |
| gc_traversal            | 4.02 ms                                                | 4.06 ms: 1.01x slower                                                      |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                      |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                      |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                     |
| async_tree_cpu_io_mixed | 739 ms                                                 | 754 ms: 1.02x slower                                                       |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                                      |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                       |
| python_startup          | 8.52 ms                                                | 8.71 ms: 1.02x slower                                                      |
| async_tree_memoization  | 627 ms                                                 | 642 ms: 1.02x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 78.2 ms: 1.03x slower                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                       |
| generators              | 73.5 ms                                                | 75.5 ms: 1.03x slower                                                      |
| meteor_contest          | 107 ms                                                 | 111 ms: 1.04x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.25 ms: 1.04x slower                                                      |
| unpack_sequence         | 43.1 ns                                                | 45.1 ns: 1.05x slower                                                      |
| regex_dna               | 204 ms                                                 | 216 ms: 1.06x slower                                                       |
| dask                    | 360 ms                                                 | 504 ms: 1.40x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (10): spectral_norm, djangocms, async_tree_none, pickle_list, bench_mp_pool, pickle_dict, deepcopy_reduce, sqlglot_parse, nbody, pickle
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230118-3.12.0a4+-30a2b7d/bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
