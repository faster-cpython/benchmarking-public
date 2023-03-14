
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: a748e80
- commit date: 2023-01-29
- overall geometric mean: 1.02x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                                              |
| chameleon      | 6.38 ms                                                | 6.91 ms: 1.08x slower                                                             |
| docutils       | 2.60 sec                                               | 2.70 sec: 1.04x slower                                                            |
| tornado_http   | 96.5 ms                                                | 106 ms: 1.10x slower                                                              |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                                              |
| float          | 76.8 ms                                                | 79.1 ms: 1.03x slower                                                             |
| nbody          | 90.0 ms                                                | 98.0 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.9 ms: 1.02x faster                                                             |
| regex_dna      | 203 ms                                                 | 206 ms: 1.01x slower                                                              |
| regex_compile  | 136 ms                                                 | 142 ms: 1.04x slower                                                              |
| regex_effbot   | 3.46 ms                                                | 3.68 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.76 ms: 1.27x faster                                                             |
| unpickle_pure_python | 227 us                                                 | 214 us: 1.06x faster                                                              |
| xml_etree_parse      | 160 ms                                                 | 154 ms: 1.04x faster                                                              |
| unpickle_list        | 4.99 us                                                | 4.83 us: 1.03x faster                                                             |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                                             |
| pickle_pure_python   | 308 us                                                 | 311 us: 1.01x slower                                                              |
| json_loads           | 26.1 us                                                | 26.6 us: 1.02x slower                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.02x slower                                                              |
| pickle               | 9.90 us                                                | 10.4 us: 1.06x slower                                                             |
| xml_etree_generate   | 75.9 ms                                                | 81.6 ms: 1.08x slower                                                             |
| xml_etree_process    | 53.7 ms                                                | 57.8 ms: 1.08x slower                                                             |
| pickle_list          | 4.14 us                                                | 4.57 us: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.13 ms: 1.06x slower                                                             |
| python_startup_no_site | 6.04 ms                                                | 6.56 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 50.5 ms: 1.02x faster                                                             |
| mako            | 9.83 ms                                                | 10.2 ms: 1.04x slower                                                             |
| genshi_text     | 21.5 ms                                                | 22.5 ms: 1.05x slower                                                             |
| django_template | 32.3 ms                                                | 34.8 ms: 1.08x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 516 ms: 1.71x faster                                                              |
| json_dumps              | 12.4 ms                                                | 9.76 ms: 1.27x faster                                                             |
| mypy2                   | 420 ms                                                 | 360 ms: 1.17x faster                                                              |
| nqueens                 | 83.8 ms                                                | 78.1 ms: 1.07x faster                                                             |
| richards                | 46.1 ms                                                | 43.2 ms: 1.07x faster                                                             |
| unpickle_pure_python    | 227 us                                                 | 214 us: 1.06x faster                                                              |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                              |
| deltablue               | 3.66 ms                                                | 3.51 ms: 1.04x faster                                                             |
| xml_etree_parse         | 160 ms                                                 | 154 ms: 1.04x faster                                                              |
| fannkuch                | 384 ms                                                 | 370 ms: 1.04x faster                                                              |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                                              |
| mdp                     | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                            |
| logging_silent          | 98.0 ns                                                | 94.6 ns: 1.04x faster                                                             |
| hexiom                  | 6.34 ms                                                | 6.12 ms: 1.03x faster                                                             |
| unpickle_list           | 4.99 us                                                | 4.83 us: 1.03x faster                                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                             |
| pycparser               | 1.19 sec                                               | 1.16 sec: 1.02x faster                                                            |
| chaos                   | 68.7 ms                                                | 67.1 ms: 1.02x faster                                                             |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.49 ms: 1.02x faster                                                             |
| genshi_xml              | 51.4 ms                                                | 50.5 ms: 1.02x faster                                                             |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                                             |
| regex_v8                | 22.2 ms                                                | 21.9 ms: 1.02x faster                                                             |
| coroutines              | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                             |
| pickle_pure_python      | 308 us                                                 | 311 us: 1.01x slower                                                              |
| pyflate                 | 419 ms                                                 | 423 ms: 1.01x slower                                                              |
| regex_dna               | 203 ms                                                 | 206 ms: 1.01x slower                                                              |
| scimark_sor             | 115 ms                                                 | 117 ms: 1.01x slower                                                              |
| crypto_pyaes            | 75.7 ms                                                | 76.9 ms: 1.02x slower                                                             |
| sympy_integrate         | 21.0 ms                                                | 21.3 ms: 1.02x slower                                                             |
| async_generators        | 356 ms                                                 | 362 ms: 1.02x slower                                                              |
| json_loads              | 26.1 us                                                | 26.6 us: 1.02x slower                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.02x slower                                                              |
| pathlib                 | 18.1 ms                                                | 18.5 ms: 1.02x slower                                                             |
| coverage                | 99.3 ms                                                | 102 ms: 1.02x slower                                                              |
| async_tree_none         | 526 ms                                                 | 540 ms: 1.03x slower                                                              |
| bench_thread_pool       | 817 us                                                 | 838 us: 1.03x slower                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.50 sec: 1.03x slower                                                            |
| float                   | 76.8 ms                                                | 79.1 ms: 1.03x slower                                                             |
| deepcopy_reduce         | 3.02 us                                                | 3.12 us: 1.03x slower                                                             |
| async_tree_io           | 1.30 sec                                               | 1.35 sec: 1.03x slower                                                            |
| docutils                | 2.60 sec                                               | 2.70 sec: 1.04x slower                                                            |
| sympy_str               | 291 ms                                                 | 302 ms: 1.04x slower                                                              |
| 2to3                    | 259 ms                                                 | 269 ms: 1.04x slower                                                              |
| telco                   | 6.43 ms                                                | 6.67 ms: 1.04x slower                                                             |
| mako                    | 9.83 ms                                                | 10.2 ms: 1.04x slower                                                             |
| sympy_sum               | 166 ms                                                 | 172 ms: 1.04x slower                                                              |
| scimark_monte_carlo     | 68.0 ms                                                | 70.7 ms: 1.04x slower                                                             |
| pprint_safe_repr        | 706 ms                                                 | 736 ms: 1.04x slower                                                              |
| regex_compile           | 136 ms                                                 | 142 ms: 1.04x slower                                                              |
| generators              | 73.5 ms                                                | 76.8 ms: 1.04x slower                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                 | 770 ms: 1.05x slower                                                              |
| genshi_text             | 21.5 ms                                                | 22.5 ms: 1.05x slower                                                             |
| scimark_lu              | 108 ms                                                 | 113 ms: 1.05x slower                                                              |
| sympy_expand            | 475 ms                                                 | 499 ms: 1.05x slower                                                              |
| sqlglot_optimize        | 52.7 ms                                                | 55.4 ms: 1.05x slower                                                             |
| raytrace                | 291 ms                                                 | 307 ms: 1.05x slower                                                              |
| dask                    | 365 ms                                                 | 385 ms: 1.05x slower                                                              |
| json                    | 4.87 ms                                                | 5.14 ms: 1.06x slower                                                             |
| pickle                  | 9.90 us                                                | 10.4 us: 1.06x slower                                                             |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                                             |
| meteor_contest          | 104 ms                                                 | 111 ms: 1.06x slower                                                              |
| logging_simple          | 6.02 us                                                | 6.40 us: 1.06x slower                                                             |
| deepcopy_memo           | 35.8 us                                                | 38.1 us: 1.06x slower                                                             |
| deepcopy                | 341 us                                                 | 363 us: 1.06x slower                                                              |
| unpack_sequence         | 44.5 ns                                                | 47.3 ns: 1.06x slower                                                             |
| python_startup          | 8.58 ms                                                | 9.13 ms: 1.06x slower                                                             |
| regex_effbot            | 3.46 ms                                                | 3.68 ms: 1.07x slower                                                             |
| sqlglot_normalize       | 108 ms                                                 | 115 ms: 1.07x slower                                                              |
| dulwich_log             | 64.0 ms                                                | 68.4 ms: 1.07x slower                                                             |
| spectral_norm           | 98.1 ms                                                | 105 ms: 1.07x slower                                                              |
| xml_etree_generate      | 75.9 ms                                                | 81.6 ms: 1.08x slower                                                             |
| django_template         | 32.3 ms                                                | 34.8 ms: 1.08x slower                                                             |
| xml_etree_process       | 53.7 ms                                                | 57.8 ms: 1.08x slower                                                             |
| chameleon               | 6.38 ms                                                | 6.91 ms: 1.08x slower                                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.56 ms: 1.09x slower                                                             |
| logging_format          | 6.48 us                                                | 7.05 us: 1.09x slower                                                             |
| nbody                   | 90.0 ms                                                | 98.0 ms: 1.09x slower                                                             |
| tornado_http            | 96.5 ms                                                | 106 ms: 1.10x slower                                                              |
| scimark_fft             | 325 ms                                                 | 357 ms: 1.10x slower                                                              |
| async_tree_memoization  | 624 ms                                                 | 687 ms: 1.10x slower                                                              |
| pickle_list             | 4.14 us                                                | 4.57 us: 1.10x slower                                                             |
| gc_traversal            | 3.82 ms                                                | 4.29 ms: 1.12x slower                                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.54 ms: 1.13x slower                                                             |
| sqlglot_transpile       | 1.65 ms                                                | 1.87 ms: 1.13x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (5): html5lib, bench_mp_pool, thrift, unpickle, djangocms
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230129-3.12.0a4+-a748e80/bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80.json: comprehensions
