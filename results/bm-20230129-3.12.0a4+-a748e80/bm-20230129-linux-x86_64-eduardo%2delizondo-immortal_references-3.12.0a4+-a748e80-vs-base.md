
# Results vs. base

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: a748e80
- commit date: 2023-01-29
- overall geometric mean: 1.05x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                 | 269 ms: 1.07x slower                                                              |
| chameleon      | 6.45 ms                                                | 6.91 ms: 1.07x slower                                                             |
| docutils       | 2.48 sec                                               | 2.70 sec: 1.09x slower                                                            |
| html5lib       | 60.1 ms                                                | 64.7 ms: 1.08x slower                                                             |
| tornado_http   | 94.4 ms                                                | 106 ms: 1.12x slower                                                              |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 189 ms                                                 | 190 ms: 1.00x slower                                                              |
| nbody          | 94.7 ms                                                | 98.0 ms: 1.04x slower                                                             |
| float          | 71.4 ms                                                | 79.1 ms: 1.11x slower                                                             |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                 | 206 ms: 1.01x faster                                                              |
| regex_v8       | 21.2 ms                                                | 21.9 ms: 1.03x slower                                                             |
| regex_effbot   | 3.46 ms                                                | 3.68 ms: 1.06x slower                                                             |
| regex_compile  | 129 ms                                                 | 142 ms: 1.10x slower                                                              |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_list        | 4.93 us                                                | 4.83 us: 1.02x faster                                                             |
| pickle_dict          | 31.0 us                                                | 30.6 us: 1.01x faster                                                             |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                             |
| json_dumps           | 9.57 ms                                                | 9.76 ms: 1.02x slower                                                             |
| xml_etree_parse      | 147 ms                                                 | 154 ms: 1.04x slower                                                              |
| xml_etree_iterparse  | 102 ms                                                 | 107 ms: 1.05x slower                                                              |
| xml_etree_generate   | 77.6 ms                                                | 81.6 ms: 1.05x slower                                                             |
| unpickle_pure_python | 201 us                                                 | 214 us: 1.06x slower                                                              |
| xml_etree_process    | 53.5 ms                                                | 57.8 ms: 1.08x slower                                                             |
| pickle_pure_python   | 284 us                                                 | 311 us: 1.09x slower                                                              |
| json_loads           | 24.1 us                                                | 26.6 us: 1.11x slower                                                             |
| pickle_list          | 4.01 us                                                | 4.57 us: 1.14x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.44 ms                                                | 6.56 ms: 1.02x slower                                                             |
| python_startup         | 8.90 ms                                                | 9.13 ms: 1.03x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.70 ms                                                | 10.2 ms: 1.05x slower                                                             |
| django_template | 32.8 ms                                                | 34.8 ms: 1.06x slower                                                             |
| genshi_xml      | 47.1 ms                                                | 50.5 ms: 1.07x slower                                                             |
| genshi_text     | 20.6 ms                                                | 22.5 ms: 1.10x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| dask                    | 500 ms                                                 | 385 ms: 1.30x faster                                                              |
| mdp                     | 2.68 sec                                               | 2.54 sec: 1.06x faster                                                            |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                              |
| unpickle_list           | 4.93 us                                                | 4.83 us: 1.02x faster                                                             |
| pickle_dict             | 31.0 us                                                | 30.6 us: 1.01x faster                                                             |
| regex_dna               | 208 ms                                                 | 206 ms: 1.01x faster                                                              |
| pidigits                | 189 ms                                                 | 190 ms: 1.00x slower                                                              |
| generators              | 76.5 ms                                                | 76.8 ms: 1.00x slower                                                             |
| create_gc_cycles        | 1.45 ms                                                | 1.47 ms: 1.01x slower                                                             |
| richards                | 42.7 ms                                                | 43.2 ms: 1.01x slower                                                             |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                             |
| sqlite_synth            | 2.58 us                                                | 2.62 us: 1.02x slower                                                             |
| async_tree_cpu_io_mixed | 758 ms                                                 | 770 ms: 1.02x slower                                                              |
| python_startup_no_site  | 6.44 ms                                                | 6.56 ms: 1.02x slower                                                             |
| json_dumps              | 9.57 ms                                                | 9.76 ms: 1.02x slower                                                             |
| logging_silent          | 92.4 ns                                                | 94.6 ns: 1.02x slower                                                             |
| thrift                  | 744 us                                                 | 761 us: 1.02x slower                                                              |
| fannkuch                | 361 ms                                                 | 370 ms: 1.03x slower                                                              |
| python_startup          | 8.90 ms                                                | 9.13 ms: 1.03x slower                                                             |
| async_tree_none         | 525 ms                                                 | 540 ms: 1.03x slower                                                              |
| async_tree_io           | 1.31 sec                                               | 1.35 sec: 1.03x slower                                                            |
| regex_v8                | 21.2 ms                                                | 21.9 ms: 1.03x slower                                                             |
| hexiom                  | 5.94 ms                                                | 6.12 ms: 1.03x slower                                                             |
| telco                   | 6.45 ms                                                | 6.67 ms: 1.03x slower                                                             |
| coverage                | 98.3 ms                                                | 102 ms: 1.03x slower                                                              |
| async_generators        | 350 ms                                                 | 362 ms: 1.03x slower                                                              |
| nbody                   | 94.7 ms                                                | 98.0 ms: 1.04x slower                                                             |
| chaos                   | 64.8 ms                                                | 67.1 ms: 1.04x slower                                                             |
| djangocms               | 31.9 us                                                | 33.1 us: 1.04x slower                                                             |
| deepcopy_reduce         | 3.00 us                                                | 3.12 us: 1.04x slower                                                             |
| coroutines              | 24.9 ms                                                | 25.9 ms: 1.04x slower                                                             |
| xml_etree_parse         | 147 ms                                                 | 154 ms: 1.04x slower                                                              |
| xml_etree_iterparse     | 102 ms                                                 | 107 ms: 1.05x slower                                                              |
| asyncio_tcp             | 494 ms                                                 | 516 ms: 1.05x slower                                                              |
| async_tree_memoization  | 656 ms                                                 | 687 ms: 1.05x slower                                                              |
| scimark_lu              | 108 ms                                                 | 113 ms: 1.05x slower                                                              |
| pycparser               | 1.10 sec                                               | 1.16 sec: 1.05x slower                                                            |
| xml_etree_generate      | 77.6 ms                                                | 81.6 ms: 1.05x slower                                                             |
| mako                    | 9.70 ms                                                | 10.2 ms: 1.05x slower                                                             |
| pathlib                 | 17.6 ms                                                | 18.5 ms: 1.05x slower                                                             |
| crypto_pyaes            | 72.9 ms                                                | 76.9 ms: 1.05x slower                                                             |
| django_template         | 32.8 ms                                                | 34.8 ms: 1.06x slower                                                             |
| pyflate                 | 399 ms                                                 | 423 ms: 1.06x slower                                                              |
| unpickle_pure_python    | 201 us                                                 | 214 us: 1.06x slower                                                              |
| regex_effbot            | 3.46 ms                                                | 3.68 ms: 1.06x slower                                                             |
| bench_thread_pool       | 786 us                                                 | 838 us: 1.07x slower                                                              |
| meteor_contest          | 104 ms                                                 | 111 ms: 1.07x slower                                                              |
| 2to3                    | 252 ms                                                 | 269 ms: 1.07x slower                                                              |
| genshi_xml              | 47.1 ms                                                | 50.5 ms: 1.07x slower                                                             |
| sympy_integrate         | 19.9 ms                                                | 21.3 ms: 1.07x slower                                                             |
| chameleon               | 6.45 ms                                                | 6.91 ms: 1.07x slower                                                             |
| spectral_norm           | 97.9 ms                                                | 105 ms: 1.07x slower                                                              |
| html5lib                | 60.1 ms                                                | 64.7 ms: 1.08x slower                                                             |
| scimark_sparse_mat_mult | 4.15 ms                                                | 4.49 ms: 1.08x slower                                                             |
| scimark_monte_carlo     | 65.5 ms                                                | 70.7 ms: 1.08x slower                                                             |
| xml_etree_process       | 53.5 ms                                                | 57.8 ms: 1.08x slower                                                             |
| pprint_pformat          | 1.39 sec                                               | 1.50 sec: 1.08x slower                                                            |
| docutils                | 2.48 sec                                               | 2.70 sec: 1.09x slower                                                            |
| sqlglot_optimize        | 51.0 ms                                                | 55.4 ms: 1.09x slower                                                             |
| sqlglot_normalize       | 105 ms                                                 | 115 ms: 1.09x slower                                                              |
| dulwich_log             | 62.9 ms                                                | 68.4 ms: 1.09x slower                                                             |
| raytrace                | 282 ms                                                 | 307 ms: 1.09x slower                                                              |
| scimark_sor             | 107 ms                                                 | 117 ms: 1.09x slower                                                              |
| pprint_safe_repr        | 675 ms                                                 | 736 ms: 1.09x slower                                                              |
| sympy_expand            | 457 ms                                                 | 499 ms: 1.09x slower                                                              |
| sqlglot_parse           | 1.41 ms                                                | 1.54 ms: 1.09x slower                                                             |
| pickle_pure_python      | 284 us                                                 | 311 us: 1.09x slower                                                              |
| genshi_text             | 20.6 ms                                                | 22.5 ms: 1.10x slower                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.87 ms: 1.10x slower                                                             |
| deepcopy_memo           | 34.7 us                                                | 38.1 us: 1.10x slower                                                             |
| deltablue               | 3.19 ms                                                | 3.51 ms: 1.10x slower                                                             |
| json                    | 4.66 ms                                                | 5.14 ms: 1.10x slower                                                             |
| regex_compile           | 129 ms                                                 | 142 ms: 1.10x slower                                                              |
| logging_simple          | 5.79 us                                                | 6.40 us: 1.10x slower                                                             |
| json_loads              | 24.1 us                                                | 26.6 us: 1.11x slower                                                             |
| float                   | 71.4 ms                                                | 79.1 ms: 1.11x slower                                                             |
| logging_format          | 6.35 us                                                | 7.05 us: 1.11x slower                                                             |
| sympy_str               | 272 ms                                                 | 302 ms: 1.11x slower                                                              |
| deepcopy                | 327 us                                                 | 363 us: 1.11x slower                                                              |
| sympy_sum               | 155 ms                                                 | 172 ms: 1.11x slower                                                              |
| tornado_http            | 94.4 ms                                                | 106 ms: 1.12x slower                                                              |
| gc_traversal            | 3.82 ms                                                | 4.29 ms: 1.12x slower                                                             |
| unpack_sequence         | 41.9 ns                                                | 47.3 ns: 1.13x slower                                                             |
| pickle_list             | 4.01 us                                                | 4.57 us: 1.14x slower                                                             |
| scimark_fft             | 308 ms                                                 | 357 ms: 1.16x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.05x slower                                                                      |

Benchmark hidden because not significant (3): unpickle, nqueens, bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20230128-3.12.0a4+-666c084/bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084.json: aiohttp, gunicorn, mypy
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20230129-3.12.0a4+-a748e80/bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80.json: comprehensions, mypy2
