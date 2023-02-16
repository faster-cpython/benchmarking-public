
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 02a1321
- commit date: 2023-01-17
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                                       |
| chameleon      | 6.38 ms                                                | 6.32 ms: 1.01x faster                                                      |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                     |
| html5lib       | 64.8 ms                                                | 61.5 ms: 1.05x faster                                                      |
| tornado_http   | 96.5 ms                                                | 94.4 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                       |
| float          | 76.8 ms                                                | 76.0 ms: 1.01x faster                                                      |
| nbody          | 90.0 ms                                                | 94.0 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                       |
| regex_v8       | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                      |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                       |
| regex_effbot   | 3.46 ms                                                | 3.65 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.34 ms: 1.32x faster                                                      |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 209 us: 1.09x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 151 ms: 1.06x faster                                                       |
| pickle_pure_python   | 308 us                                                 | 293 us: 1.05x faster                                                       |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                                      |
| pickle_list          | 4.14 us                                                | 4.08 us: 1.01x faster                                                      |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                                      |
| unpickle_list        | 4.99 us                                                | 4.93 us: 1.01x faster                                                      |
| xml_etree_process    | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                       |
| xml_etree_generate   | 75.9 ms                                                | 76.9 ms: 1.01x slower                                                      |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.74 ms: 1.02x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.27 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.2 ms: 1.11x faster                                                      |
| genshi_text     | 21.5 ms                                                | 20.2 ms: 1.07x faster                                                      |
| mako            | 9.83 ms                                                | 9.71 ms: 1.01x faster                                                      |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 494 ms: 1.79x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.34 ms: 1.32x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 46.2 ms: 1.11x faster                                                      |
| logging_silent          | 98.0 ns                                                | 89.6 ns: 1.09x faster                                                      |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 209 us: 1.09x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.26 ms: 1.08x faster                                                      |
| sympy_str               | 291 ms                                                 | 271 ms: 1.07x faster                                                       |
| nqueens                 | 83.8 ms                                                | 78.0 ms: 1.07x faster                                                      |
| json                    | 4.87 ms                                                | 4.56 ms: 1.07x faster                                                      |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| genshi_text             | 21.5 ms                                                | 20.2 ms: 1.07x faster                                                      |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.06x faster                                                     |
| gc_traversal            | 3.82 ms                                                | 3.59 ms: 1.06x faster                                                      |
| chaos                   | 68.7 ms                                                | 64.7 ms: 1.06x faster                                                      |
| xml_etree_parse         | 160 ms                                                 | 151 ms: 1.06x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                     |
| hexiom                  | 6.34 ms                                                | 6.00 ms: 1.06x faster                                                      |
| html5lib                | 64.8 ms                                                | 61.5 ms: 1.05x faster                                                      |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                                       |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                       |
| pickle_pure_python      | 308 us                                                 | 293 us: 1.05x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 998 us: 1.05x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 34.1 us: 1.05x faster                                                      |
| crypto_pyaes            | 75.7 ms                                                | 72.0 ms: 1.05x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                      |
| scimark_fft             | 325 ms                                                 | 310 ms: 1.05x faster                                                       |
| deepcopy                | 341 us                                                 | 326 us: 1.05x faster                                                       |
| bench_thread_pool       | 817 us                                                 | 782 us: 1.04x faster                                                       |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.50 ms: 1.04x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                      |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                     |
| logging_simple          | 6.02 us                                                | 5.81 us: 1.04x faster                                                      |
| regex_v8                | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                      |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                                      |
| thrift                  | 760 us                                                 | 738 us: 1.03x faster                                                       |
| coverage                | 99.3 ms                                                | 96.7 ms: 1.03x faster                                                      |
| dulwich_log             | 64.0 ms                                                | 62.4 ms: 1.03x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                                      |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                       |
| coroutines              | 26.2 ms                                                | 25.6 ms: 1.02x faster                                                      |
| unpack_sequence         | 44.5 ns                                                | 43.5 ns: 1.02x faster                                                      |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                      |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                      |
| tornado_http            | 96.5 ms                                                | 94.4 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                       |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                                      |
| async_generators        | 356 ms                                                 | 350 ms: 1.02x faster                                                       |
| pickle_list             | 4.14 us                                                | 4.08 us: 1.01x faster                                                      |
| telco                   | 6.43 ms                                                | 6.34 ms: 1.01x faster                                                      |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                       |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                       |
| 2to3                    | 259 ms                                                 | 256 ms: 1.01x faster                                                       |
| mako                    | 9.83 ms                                                | 9.71 ms: 1.01x faster                                                      |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                                      |
| float                   | 76.8 ms                                                | 76.0 ms: 1.01x faster                                                      |
| unpickle_list           | 4.99 us                                                | 4.93 us: 1.01x faster                                                      |
| xml_etree_process       | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                      |
| chameleon               | 6.38 ms                                                | 6.32 ms: 1.01x faster                                                      |
| mdp                     | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                     |
| pyflate                 | 419 ms                                                 | 420 ms: 1.00x slower                                                       |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                                       |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                                      |
| xml_etree_generate      | 75.9 ms                                                | 76.9 ms: 1.01x slower                                                      |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                      |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.02x slower                                                       |
| python_startup          | 8.58 ms                                                | 8.74 ms: 1.02x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 637 ms: 1.02x slower                                                       |
| generators              | 73.5 ms                                                | 75.2 ms: 1.02x slower                                                      |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                       |
| raytrace                | 291 ms                                                 | 299 ms: 1.03x slower                                                       |
| scimark_monte_carlo     | 68.0 ms                                                | 69.8 ms: 1.03x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                 | 763 ms: 1.04x slower                                                       |
| python_startup_no_site  | 6.04 ms                                                | 6.27 ms: 1.04x slower                                                      |
| scimark_sor             | 115 ms                                                 | 119 ms: 1.04x slower                                                       |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                      |
| nbody                   | 90.0 ms                                                | 94.0 ms: 1.04x slower                                                      |
| regex_effbot            | 3.46 ms                                                | 3.65 ms: 1.06x slower                                                      |
| dask                    | 365 ms                                                 | 512 ms: 1.40x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (7): async_tree_none, spectral_norm, logging_format, bench_mp_pool, fannkuch, djangocms, richards
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-02a1321/bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321.json: mypy
