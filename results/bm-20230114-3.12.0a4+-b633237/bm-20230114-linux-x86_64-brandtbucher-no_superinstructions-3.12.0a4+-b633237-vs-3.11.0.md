
# Results vs. 3.11.0

- fork: brandtbucher
- ref: no_superinstructions
- machine: linux-x86_64
- commit hash: b633237
- commit date: 2023-01-14
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 255 ms: 1.02x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.49 ms: 1.02x slower                                                        |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                       |
| html5lib       | 64.8 ms                                                | 60.6 ms: 1.07x faster                                                        |
| tornado_http   | 96.5 ms                                                | 94.9 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                        |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| nbody          | 90.0 ms                                                | 94.2 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                        |
| regex_compile  | 136 ms                                                 | 133 ms: 1.03x faster                                                         |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                         |
| regex_effbot   | 3.46 ms                                                | 3.54 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.38 ms: 1.32x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                                         |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.08x faster                                                         |
| pickle_dict          | 31.2 us                                                | 29.5 us: 1.06x faster                                                        |
| pickle_list          | 4.14 us                                                | 4.02 us: 1.03x faster                                                        |
| unpickle             | 13.3 us                                                | 12.9 us: 1.03x faster                                                        |
| unpickle_list        | 4.99 us                                                | 4.91 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                         |
| xml_etree_generate   | 75.9 ms                                                | 77.0 ms: 1.01x slower                                                        |
| pickle               | 9.90 us                                                | 10.0 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.74 ms: 1.02x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.30 ms: 1.04x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.1 ms: 1.09x faster                                                        |
| genshi_text     | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                        |
| mako            | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                        |
| django_template | 32.3 ms                                                | 32.7 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 504 ms: 1.75x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.38 ms: 1.32x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.23 ms: 1.13x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.13 ms: 1.11x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 47.1 ms: 1.09x faster                                                        |
| gc_traversal            | 3.82 ms                                                | 3.50 ms: 1.09x faster                                                        |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.08x faster                                                         |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                         |
| logging_silent          | 98.0 ns                                                | 91.7 ns: 1.07x faster                                                        |
| html5lib                | 64.8 ms                                                | 60.6 ms: 1.07x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                       |
| float                   | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                        |
| pickle_dict             | 31.2 us                                                | 29.5 us: 1.06x faster                                                        |
| nqueens                 | 83.8 ms                                                | 79.4 ms: 1.06x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.44 ms: 1.05x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                       |
| pyflate                 | 419 ms                                                 | 398 ms: 1.05x faster                                                         |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                        |
| richards                | 46.1 ms                                                | 44.0 ms: 1.05x faster                                                        |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                                        |
| coroutines              | 26.2 ms                                                | 25.0 ms: 1.04x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 676 ms: 1.04x faster                                                         |
| bench_thread_pool       | 817 us                                                 | 784 us: 1.04x faster                                                         |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                       |
| json                    | 4.87 ms                                                | 4.71 ms: 1.03x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.82 us: 1.03x faster                                                        |
| pickle_list             | 4.14 us                                                | 4.02 us: 1.03x faster                                                        |
| coverage                | 99.3 ms                                                | 96.2 ms: 1.03x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                        |
| unpickle                | 13.3 us                                                | 12.9 us: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 66.1 ms: 1.03x faster                                                        |
| scimark_fft             | 325 ms                                                 | 317 ms: 1.03x faster                                                         |
| fannkuch                | 384 ms                                                 | 374 ms: 1.03x faster                                                         |
| go                      | 140 ms                                                 | 137 ms: 1.03x faster                                                         |
| regex_compile           | 136 ms                                                 | 133 ms: 1.03x faster                                                         |
| hexiom                  | 6.34 ms                                                | 6.18 ms: 1.03x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 62.4 ms: 1.03x faster                                                        |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.03x faster                                                        |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                        |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                                         |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                        |
| tornado_http            | 96.5 ms                                                | 94.9 ms: 1.02x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| deepcopy                | 341 us                                                 | 336 us: 1.02x faster                                                         |
| unpickle_list           | 4.99 us                                                | 4.91 us: 1.02x faster                                                        |
| 2to3                    | 259 ms                                                 | 255 ms: 1.02x faster                                                         |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.01x faster                                                         |
| thrift                  | 760 us                                                 | 750 us: 1.01x faster                                                         |
| raytrace                | 291 ms                                                 | 288 ms: 1.01x faster                                                         |
| sympy_str               | 291 ms                                                 | 288 ms: 1.01x faster                                                         |
| mdp                     | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                       |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                         |
| mako                    | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                        |
| logging_format          | 6.48 us                                                | 6.52 us: 1.01x slower                                                        |
| deepcopy_memo           | 35.8 us                                                | 36.1 us: 1.01x slower                                                        |
| pathlib                 | 18.1 ms                                                | 18.2 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                                         |
| django_template         | 32.3 ms                                                | 32.7 ms: 1.01x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 77.0 ms: 1.01x slower                                                        |
| generators              | 73.5 ms                                                | 74.6 ms: 1.01x slower                                                        |
| pickle                  | 9.90 us                                                | 10.0 us: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                       |
| chameleon               | 6.38 ms                                                | 6.49 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 749 ms: 1.02x slower                                                         |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                         |
| python_startup          | 8.58 ms                                                | 8.74 ms: 1.02x slower                                                        |
| regex_effbot            | 3.46 ms                                                | 3.54 ms: 1.02x slower                                                        |
| chaos                   | 68.7 ms                                                | 70.4 ms: 1.03x slower                                                        |
| crypto_pyaes            | 75.7 ms                                                | 77.7 ms: 1.03x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.30 ms: 1.04x slower                                                        |
| nbody                   | 90.0 ms                                                | 94.2 ms: 1.05x slower                                                        |
| async_tree_memoization  | 624 ms                                                 | 658 ms: 1.05x slower                                                         |
| unpack_sequence         | 44.5 ns                                                | 49.0 ns: 1.10x slower                                                        |
| dask                    | 365 ms                                                 | 507 ms: 1.39x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (8): sympy_sum, spectral_norm, async_generators, bench_mp_pool, telco, xml_etree_process, async_tree_none, djangocms
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230114-3.12.0a4+-b633237/bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237.json: mypy
