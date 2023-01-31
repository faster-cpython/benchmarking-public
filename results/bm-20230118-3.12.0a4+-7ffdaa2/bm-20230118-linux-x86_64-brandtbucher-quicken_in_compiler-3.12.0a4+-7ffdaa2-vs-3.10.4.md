
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 7ffdaa2
- commit date: 2023-01-18
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 250 ms: 1.33x faster                                                        |
| chameleon      | 8.86 ms                                                | 6.28 ms: 1.41x faster                                                       |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                      |
| html5lib       | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                       |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.0 ms: 1.50x faster                                                       |
| nbody          | 136 ms                                                 | 93.9 ms: 1.45x faster                                                       |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.35x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                        |
| regex_effbot   | 3.21 ms                                                | 3.44 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 280 us: 1.62x faster                                                        |
| unpickle_pure_python | 297 us                                                 | 196 us: 1.51x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.45 ms: 1.43x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                       |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                                       |
| xml_etree_generate   | 93.3 ms                                                | 77.9 ms: 1.20x faster                                                       |
| pickle_list          | 4.50 us                                                | 4.04 us: 1.11x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| unpickle             | 14.3 us                                                | 13.3 us: 1.08x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                 | 105 ms: 1.06x faster                                                        |
| pickle               | 10.1 us                                                | 10.1 us: 1.01x faster                                                       |
| unpickle_list        | 4.99 us                                                | 5.11 us: 1.02x slower                                                       |
| pickle_dict          | 28.3 us                                                | 31.0 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.84 ms: 1.58x faster                                                       |
| python_startup_no_site | 5.76 ms                                                | 6.39 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| mako            | 14.3 ms                                                | 9.75 ms: 1.46x faster                                                       |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                       |
| genshi_xml      | 63.6 ms                                                | 46.6 ms: 1.37x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.28 ms: 2.26x faster                                                       |
| logging_silent          | 173 ns                                                 | 92.1 ns: 1.88x faster                                                       |
| scimark_sor             | 193 ms                                                 | 104 ms: 1.86x faster                                                        |
| pyflate                 | 675 ms                                                 | 391 ms: 1.73x faster                                                        |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                        |
| richards                | 71.4 ms                                                | 42.1 ms: 1.69x faster                                                       |
| raytrace                | 461 ms                                                 | 280 ms: 1.65x faster                                                        |
| pickle_pure_python      | 453 us                                                 | 280 us: 1.62x faster                                                        |
| chaos                   | 104 ms                                                 | 64.4 ms: 1.62x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 73.2 ms: 1.60x faster                                                       |
| scimark_monte_carlo     | 105 ms                                                 | 66.0 ms: 1.59x faster                                                       |
| hexiom                  | 9.42 ms                                                | 5.95 ms: 1.58x faster                                                       |
| python_startup          | 13.9 ms                                                | 8.84 ms: 1.58x faster                                                       |
| spectral_norm           | 148 ms                                                 | 94.4 ms: 1.57x faster                                                       |
| unpickle_pure_python    | 297 us                                                 | 196 us: 1.51x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| float                   | 108 ms                                                 | 72.0 ms: 1.50x faster                                                       |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                        |
| mako                    | 14.3 ms                                                | 9.75 ms: 1.46x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                                       |
| nbody                   | 136 ms                                                 | 93.9 ms: 1.45x faster                                                       |
| deepcopy_memo           | 50.0 us                                                | 34.5 us: 1.45x faster                                                       |
| html5lib                | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                       |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.45 ms: 1.43x faster                                                       |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                       |
| chameleon               | 8.86 ms                                                | 6.28 ms: 1.41x faster                                                       |
| pprint_pformat          | 1.97 sec                                               | 1.41 sec: 1.40x faster                                                      |
| logging_format          | 8.92 us                                                | 6.37 us: 1.40x faster                                                       |
| scimark_fft             | 414 ms                                                 | 296 ms: 1.40x faster                                                        |
| logging_simple          | 8.06 us                                                | 5.77 us: 1.40x faster                                                       |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.93 ms: 1.39x faster                                                       |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                       |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.37x faster                                                       |
| genshi_xml              | 63.6 ms                                                | 46.6 ms: 1.37x faster                                                       |
| async_tree_none         | 713 ms                                                 | 525 ms: 1.36x faster                                                        |
| pycparser               | 1.51 sec                                               | 1.12 sec: 1.35x faster                                                      |
| regex_compile           | 174 ms                                                 | 128 ms: 1.35x faster                                                        |
| pprint_safe_repr        | 943 ms                                                 | 696 ms: 1.35x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 992 us: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                      |
| unpack_sequence         | 59.5 ns                                                | 44.3 ns: 1.34x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                       |
| 2to3                    | 332 ms                                                 | 250 ms: 1.33x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 653 ms: 1.31x faster                                                        |
| nqueens                 | 99.3 ms                                                | 76.3 ms: 1.30x faster                                                       |
| deepcopy                | 429 us                                                 | 332 us: 1.29x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                        |
| fannkuch                | 477 ms                                                 | 371 ms: 1.29x faster                                                        |
| coroutines              | 31.7 ms                                                | 24.6 ms: 1.28x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                       |
| deepcopy_reduce         | 3.75 us                                                | 2.96 us: 1.27x faster                                                       |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                      |
| mypy                    | 1.01 sec                                               | 805 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                        |
| async_generators        | 428 ms                                                 | 351 ms: 1.22x faster                                                        |
| dulwich_log             | 75.5 ms                                                | 62.1 ms: 1.21x faster                                                       |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                                       |
| bench_thread_pool       | 943 us                                                 | 780 us: 1.21x faster                                                        |
| sympy_str               | 324 ms                                                 | 269 ms: 1.21x faster                                                        |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                                       |
| xml_etree_generate      | 93.3 ms                                                | 77.9 ms: 1.20x faster                                                       |
| sympy_expand            | 537 ms                                                 | 452 ms: 1.19x faster                                                        |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                        |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                                       |
| sqlite_synth            | 2.90 us                                                | 2.57 us: 1.13x faster                                                       |
| pickle_list             | 4.50 us                                                | 4.04 us: 1.11x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                        |
| unpickle                | 14.3 us                                                | 13.3 us: 1.08x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.66 sec: 1.06x faster                                                      |
| xml_etree_iterparse     | 110 ms                                                 | 105 ms: 1.06x faster                                                        |
| telco                   | 6.68 ms                                                | 6.37 ms: 1.05x faster                                                       |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                        |
| generators              | 75.8 ms                                                | 75.0 ms: 1.01x faster                                                       |
| pickle                  | 10.1 us                                                | 10.1 us: 1.01x faster                                                       |
| unpickle_list           | 4.99 us                                                | 5.11 us: 1.02x slower                                                       |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                        |
| regex_effbot            | 3.21 ms                                                | 3.44 ms: 1.07x slower                                                       |
| pickle_dict             | 28.3 us                                                | 31.0 us: 1.09x slower                                                       |
| python_startup_no_site  | 5.76 ms                                                | 6.39 ms: 1.11x slower                                                       |
| coverage                | 75.3 ms                                                | 95.3 ms: 1.27x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-7ffdaa2/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
