
# Results vs. 3.11.0

- fork: brandtbucher
- ref: add_small_int_new
- machine: linux-x86_64
- commit hash: 114cba6
- commit date: 2023-03-20
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                      |
| chameleon      | 6.38 ms                                                | 6.32 ms: 1.01x faster                                                     |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                    |
| html5lib       | 64.8 ms                                                | 60.4 ms: 1.07x faster                                                     |
| tornado_http   | 96.5 ms                                                | 91.1 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.5 ms: 1.04x faster                                                     |
| nbody          | 90.0 ms                                                | 87.7 ms: 1.03x faster                                                     |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.4 ms: 1.04x faster                                                     |
| regex_compile  | 136 ms                                                 | 133 ms: 1.02x faster                                                      |
| regex_effbot   | 3.46 ms                                                | 3.50 ms: 1.01x slower                                                     |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.53 ms: 1.30x faster                                                     |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                      |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                                      |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                      |
| json_loads           | 26.1 us                                                | 24.4 us: 1.07x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 99.1 ms: 1.05x faster                                                     |
| pickle_dict          | 31.2 us                                                | 31.4 us: 1.01x slower                                                     |
| pickle_list          | 4.14 us                                                | 4.20 us: 1.01x slower                                                     |
| unpickle_list        | 4.99 us                                                | 5.12 us: 1.03x slower                                                     |
| xml_etree_process    | 53.7 ms                                                | 55.3 ms: 1.03x slower                                                     |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                     |
| xml_etree_generate   | 75.9 ms                                                | 80.8 ms: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.89 ms: 1.04x slower                                                     |
| python_startup_no_site | 6.04 ms                                                | 6.51 ms: 1.08x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.4 ms: 1.09x faster                                                     |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                     |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                     |
| mako            | 9.83 ms                                                | 10.1 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                                     |
| asyncio_tcp             | 883 ms                                                 | 507 ms: 1.74x faster                                                      |
| json_dumps              | 12.4 ms                                                | 9.53 ms: 1.30x faster                                                     |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                      |
| coroutines              | 26.2 ms                                                | 22.5 ms: 1.16x faster                                                     |
| deltablue               | 3.66 ms                                                | 3.15 ms: 1.16x faster                                                     |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                      |
| richards                | 46.1 ms                                                | 41.8 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.19 ms: 1.10x faster                                                     |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 47.4 ms: 1.09x faster                                                     |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                      |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                      |
| html5lib                | 64.8 ms                                                | 60.4 ms: 1.07x faster                                                     |
| json_loads              | 26.1 us                                                | 24.4 us: 1.07x faster                                                     |
| scimark_fft             | 325 ms                                                 | 306 ms: 1.06x faster                                                      |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                      |
| deepcopy                | 341 us                                                 | 322 us: 1.06x faster                                                      |
| tornado_http            | 96.5 ms                                                | 91.1 ms: 1.06x faster                                                     |
| nqueens                 | 83.8 ms                                                | 79.1 ms: 1.06x faster                                                     |
| fannkuch                | 384 ms                                                 | 363 ms: 1.06x faster                                                      |
| deepcopy_memo           | 35.8 us                                                | 33.9 us: 1.06x faster                                                     |
| json                    | 4.87 ms                                                | 4.63 ms: 1.05x faster                                                     |
| raytrace                | 291 ms                                                 | 277 ms: 1.05x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                    |
| logging_simple          | 6.02 us                                                | 5.73 us: 1.05x faster                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 99.1 ms: 1.05x faster                                                     |
| chaos                   | 68.7 ms                                                | 65.4 ms: 1.05x faster                                                     |
| mdp                     | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                    |
| float                   | 76.8 ms                                                | 73.5 ms: 1.04x faster                                                     |
| coverage                | 99.3 ms                                                | 95.1 ms: 1.04x faster                                                     |
| deepcopy_reduce         | 3.02 us                                                | 2.89 us: 1.04x faster                                                     |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                     |
| hexiom                  | 6.34 ms                                                | 6.09 ms: 1.04x faster                                                     |
| regex_v8                | 22.2 ms                                                | 21.4 ms: 1.04x faster                                                     |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 788 us: 1.04x faster                                                      |
| sympy_expand            | 475 ms                                                 | 461 ms: 1.03x faster                                                      |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                                     |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                     |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                                      |
| pprint_safe_repr        | 706 ms                                                 | 686 ms: 1.03x faster                                                      |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                     |
| nbody                   | 90.0 ms                                                | 87.7 ms: 1.03x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                     |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                     |
| unpack_sequence         | 44.5 ns                                                | 43.3 ns: 1.03x faster                                                     |
| pycparser               | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                    |
| regex_compile           | 136 ms                                                 | 133 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                      |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                      |
| pyflate                 | 419 ms                                                 | 410 ms: 1.02x faster                                                      |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                    |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                                     |
| logging_silent          | 98.0 ns                                                | 96.0 ns: 1.02x faster                                                     |
| scimark_monte_carlo     | 68.0 ms                                                | 66.6 ms: 1.02x faster                                                     |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.02x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.49 ms: 1.01x faster                                                     |
| dulwich_log             | 64.0 ms                                                | 63.0 ms: 1.01x faster                                                     |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| crypto_pyaes            | 75.7 ms                                                | 75.0 ms: 1.01x faster                                                     |
| chameleon               | 6.38 ms                                                | 6.32 ms: 1.01x faster                                                     |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                    |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                     |
| pickle_dict             | 31.2 us                                                | 31.4 us: 1.01x slower                                                     |
| regex_effbot            | 3.46 ms                                                | 3.50 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed | 736 ms                                                 | 746 ms: 1.01x slower                                                      |
| pickle_list             | 4.14 us                                                | 4.20 us: 1.01x slower                                                     |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                      |
| pathlib                 | 18.1 ms                                                | 18.5 ms: 1.02x slower                                                     |
| mako                    | 9.83 ms                                                | 10.1 ms: 1.02x slower                                                     |
| thrift                  | 760 us                                                 | 777 us: 1.02x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 640 ms: 1.03x slower                                                      |
| unpickle_list           | 4.99 us                                                | 5.12 us: 1.03x slower                                                     |
| gc_traversal            | 3.82 ms                                                | 3.93 ms: 1.03x slower                                                     |
| xml_etree_process       | 53.7 ms                                                | 55.3 ms: 1.03x slower                                                     |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                      |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                     |
| python_startup          | 8.58 ms                                                | 8.89 ms: 1.04x slower                                                     |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                                     |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                     |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                     |
| xml_etree_generate      | 75.9 ms                                                | 80.8 ms: 1.06x slower                                                     |
| python_startup_no_site  | 6.04 ms                                                | 6.51 ms: 1.08x slower                                                     |
| async_generators        | 356 ms                                                 | 413 ms: 1.16x slower                                                      |
| dask                    | 365 ms                                                 | 503 ms: 1.38x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (7): djangocms, async_tree_none, sympy_sum, spectral_norm, bench_mp_pool, telco, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230320-3.12.0a6+-114cba6/bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6.json: comprehensions
