
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache_fixed
- machine: linux-x86_64
- commit hash: 212046c
- commit date: 2023-03-23
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                   |
| html5lib       | 64.5 ms                                                | 61.6 ms: 1.05x faster                                                    |
| tornado_http   | 96.3 ms                                                | 92.5 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.8 ms: 1.06x faster                                                    |
| float          | 77.2 ms                                                | 73.1 ms: 1.06x faster                                                    |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.37 ms: 1.18x faster                                                    |
| regex_compile  | 138 ms                                                 | 132 ms: 1.04x faster                                                     |
| regex_v8       | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                    |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.56 ms: 1.32x faster                                                    |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                                     |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                                    |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 99.2 ms: 1.05x faster                                                    |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                    |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                    |
| pickle_list          | 4.11 us                                                | 4.27 us: 1.04x slower                                                    |
| xml_etree_process    | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                    |
| xml_etree_generate   | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                    |
| unpickle_list        | 4.91 us                                                | 5.25 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.82 ms: 1.03x slower                                                    |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.4 ms: 1.07x faster                                                    |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.8 ms: 2.47x faster                                                    |
| asyncio_tcp             | 922 ms                                                 | 510 ms: 1.81x faster                                                     |
| json_dumps              | 12.6 ms                                                | 9.56 ms: 1.32x faster                                                    |
| mypy2                   | 420 ms                                                 | 335 ms: 1.25x faster                                                     |
| regex_effbot            | 3.99 ms                                                | 3.37 ms: 1.18x faster                                                    |
| gc_traversal            | 4.02 ms                                                | 3.53 ms: 1.14x faster                                                    |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                                     |
| coroutines              | 25.5 ms                                                | 22.6 ms: 1.13x faster                                                    |
| deltablue               | 3.67 ms                                                | 3.27 ms: 1.12x faster                                                    |
| spectral_norm           | 100 ms                                                 | 90.9 ms: 1.10x faster                                                    |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                    |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                                    |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.08x faster                                                     |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                    |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 48.4 ms: 1.07x faster                                                    |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                                    |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                                     |
| nbody                   | 93.1 ms                                                | 87.8 ms: 1.06x faster                                                    |
| float                   | 77.2 ms                                                | 73.1 ms: 1.06x faster                                                    |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                     |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                                    |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                     |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                     |
| nqueens                 | 83.4 ms                                                | 79.4 ms: 1.05x faster                                                    |
| fannkuch                | 388 ms                                                 | 370 ms: 1.05x faster                                                     |
| hexiom                  | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                    |
| html5lib                | 64.5 ms                                                | 61.6 ms: 1.05x faster                                                    |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.29 ms: 1.05x faster                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 99.2 ms: 1.05x faster                                                    |
| regex_compile           | 138 ms                                                 | 132 ms: 1.04x faster                                                     |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                                   |
| tornado_http            | 96.3 ms                                                | 92.5 ms: 1.04x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                   |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                   |
| chaos                   | 69.2 ms                                                | 66.6 ms: 1.04x faster                                                    |
| logging_silent          | 101 ns                                                 | 97.5 ns: 1.04x faster                                                    |
| richards                | 45.7 ms                                                | 44.1 ms: 1.04x faster                                                    |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                     |
| logging_format          | 6.68 us                                                | 6.46 us: 1.03x faster                                                    |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| unpack_sequence         | 43.1 ns                                                | 41.7 ns: 1.03x faster                                                    |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                                     |
| coverage                | 100 ms                                                 | 97.0 ms: 1.03x faster                                                    |
| bench_thread_pool       | 819 us                                                 | 794 us: 1.03x faster                                                     |
| raytrace                | 297 ms                                                 | 288 ms: 1.03x faster                                                     |
| sqlglot_optimize        | 53.1 ms                                                | 51.8 ms: 1.03x faster                                                    |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                    |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                     |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                                     |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                                     |
| telco                   | 6.58 ms                                                | 6.45 ms: 1.02x faster                                                    |
| logging_simple          | 6.03 us                                                | 5.91 us: 1.02x faster                                                    |
| regex_v8                | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                    |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                    |
| scimark_monte_carlo     | 68.1 ms                                                | 67.0 ms: 1.02x faster                                                    |
| crypto_pyaes            | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 107 ms: 1.01x faster                                                     |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                                    |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                    |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                     |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 749 ms: 1.01x slower                                                     |
| scimark_lu              | 110 ms                                                 | 111 ms: 1.02x slower                                                     |
| deepcopy_reduce         | 2.94 us                                                | 3.00 us: 1.02x slower                                                    |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                                    |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                    |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                                    |
| python_startup          | 8.52 ms                                                | 8.82 ms: 1.03x slower                                                    |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.03x slower                                                    |
| pickle_list             | 4.11 us                                                | 4.27 us: 1.04x slower                                                    |
| xml_etree_process       | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                    |
| thrift                  | 756 us                                                 | 792 us: 1.05x slower                                                     |
| xml_etree_generate      | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                    |
| comprehensions          | 22.4 us                                                | 24.0 us: 1.07x slower                                                    |
| unpickle_list           | 4.91 us                                                | 5.25 us: 1.07x slower                                                    |
| async_tree_memoization  | 627 ms                                                 | 673 ms: 1.07x slower                                                     |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                    |
| async_generators        | 368 ms                                                 | 416 ms: 1.13x slower                                                     |
| dask                    | 360 ms                                                 | 512 ms: 1.42x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (10): unpickle, async_tree_none, sympy_sum, bench_mp_pool, djangocms, pyflate, mako, chameleon, dulwich_log, genshi_text
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
