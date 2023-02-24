
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 39ace64
- commit date: 2023-02-22
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.43 ms: 1.01x slower                                                        |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                       |
| html5lib       | 64.8 ms                                                | 61.8 ms: 1.05x faster                                                        |
| tornado_http   | 96.5 ms                                                | 94.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.4 ms: 1.05x faster                                                        |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| nbody          | 90.0 ms                                                | 96.7 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| regex_v8       | 22.2 ms                                                | 22.0 ms: 1.01x faster                                                        |
| regex_effbot   | 3.46 ms                                                | 3.52 ms: 1.02x slower                                                        |
| regex_dna      | 203 ms                                                 | 216 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.43 ms: 1.31x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.14x faster                                                         |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                                         |
| xml_etree_parse      | 160 ms                                                 | 150 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 99.5 ms: 1.05x faster                                                        |
| pickle_list          | 4.14 us                                                | 4.03 us: 1.03x faster                                                        |
| pickle_dict          | 31.2 us                                                | 30.9 us: 1.01x faster                                                        |
| unpickle_list        | 4.99 us                                                | 5.02 us: 1.01x slower                                                        |
| xml_etree_process    | 53.7 ms                                                | 54.6 ms: 1.02x slower                                                        |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 80.4 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.7 ms: 1.10x faster                                                        |
| genshi_text     | 21.5 ms                                                | 20.7 ms: 1.04x faster                                                        |
| mako            | 9.83 ms                                                | 9.80 ms: 1.00x faster                                                        |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.6 ms: 2.49x faster                                                        |
| asyncio_tcp             | 883 ms                                                 | 501 ms: 1.76x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.43 ms: 1.31x faster                                                        |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                         |
| coroutines              | 26.2 ms                                                | 22.4 ms: 1.17x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.14 ms: 1.16x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.14x faster                                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.02 ms: 1.14x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 46.7 ms: 1.10x faster                                                        |
| richards                | 46.1 ms                                                | 42.4 ms: 1.09x faster                                                        |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                                       |
| logging_silent          | 98.0 ns                                                | 90.4 ns: 1.08x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                                         |
| hexiom                  | 6.34 ms                                                | 5.90 ms: 1.07x faster                                                        |
| nqueens                 | 83.8 ms                                                | 78.1 ms: 1.07x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 150 ms: 1.06x faster                                                         |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| json                    | 4.87 ms                                                | 4.58 ms: 1.06x faster                                                        |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                                         |
| fannkuch                | 384 ms                                                 | 364 ms: 1.06x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 102 ms: 1.05x faster                                                         |
| scimark_fft             | 325 ms                                                 | 309 ms: 1.05x faster                                                         |
| sqlglot_optimize        | 52.7 ms                                                | 50.2 ms: 1.05x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 34.1 us: 1.05x faster                                                        |
| html5lib                | 64.8 ms                                                | 61.8 ms: 1.05x faster                                                        |
| unpack_sequence         | 44.5 ns                                                | 42.4 ns: 1.05x faster                                                        |
| float                   | 76.8 ms                                                | 73.4 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 99.5 ms: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                         |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                        |
| mdp                     | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                       |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                         |
| genshi_text             | 21.5 ms                                                | 20.7 ms: 1.04x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.80 us: 1.04x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 73.1 ms: 1.04x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 790 us: 1.03x faster                                                         |
| deepcopy                | 341 us                                                 | 330 us: 1.03x faster                                                         |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                        |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                         |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                        |
| deepcopy_reduce         | 3.02 us                                                | 2.93 us: 1.03x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 95.4 ms: 1.03x faster                                                        |
| pickle_list             | 4.14 us                                                | 4.03 us: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 66.2 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 688 ms: 1.03x faster                                                         |
| sympy_str               | 291 ms                                                 | 284 ms: 1.03x faster                                                         |
| chaos                   | 68.7 ms                                                | 67.0 ms: 1.03x faster                                                        |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                         |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| tornado_http            | 96.5 ms                                                | 94.5 ms: 1.02x faster                                                        |
| logging_format          | 6.48 us                                                | 6.36 us: 1.02x faster                                                        |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                       |
| pyflate                 | 419 ms                                                 | 412 ms: 1.02x faster                                                         |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                                        |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.02x faster                                                         |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                         |
| create_gc_cycles        | 1.52 ms                                                | 1.50 ms: 1.01x faster                                                        |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                         |
| coverage                | 99.3 ms                                                | 98.2 ms: 1.01x faster                                                        |
| regex_v8                | 22.2 ms                                                | 22.0 ms: 1.01x faster                                                        |
| pickle_dict             | 31.2 us                                                | 30.9 us: 1.01x faster                                                        |
| mako                    | 9.83 ms                                                | 9.80 ms: 1.00x faster                                                        |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                       |
| gc_traversal            | 3.82 ms                                                | 3.85 ms: 1.01x slower                                                        |
| unpickle_list           | 4.99 us                                                | 5.02 us: 1.01x slower                                                        |
| chameleon               | 6.38 ms                                                | 6.43 ms: 1.01x slower                                                        |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 744 ms: 1.01x slower                                                         |
| xml_etree_process       | 53.7 ms                                                | 54.6 ms: 1.02x slower                                                        |
| regex_effbot            | 3.46 ms                                                | 3.52 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.68 ms: 1.02x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.39 ms: 1.02x slower                                                        |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                        |
| python_startup          | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 80.4 ms: 1.06x slower                                                        |
| regex_dna               | 203 ms                                                 | 216 ms: 1.06x slower                                                         |
| async_tree_memoization  | 624 ms                                                 | 666 ms: 1.07x slower                                                         |
| nbody                   | 90.0 ms                                                | 96.7 ms: 1.07x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                        |
| async_generators        | 356 ms                                                 | 409 ms: 1.15x slower                                                         |
| dask                    | 365 ms                                                 | 503 ms: 1.38x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (9): sqlalchemy_imperative, telco, sympy_sum, bench_mp_pool, djangocms, async_tree_none, pathlib, thrift, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
