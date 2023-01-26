
# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_attr_managed_di
- machine: linux-x86_64
- commit hash: d5db69f
- commit date: 2023-01-17
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 250 ms: 1.33x faster                                                         |
| chameleon      | 8.86 ms                                                | 6.37 ms: 1.39x faster                                                        |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                       |
| html5lib       | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.0 ms: 1.37x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.8 ms: 1.48x faster                                                        |
| nbody          | 136 ms                                                 | 92.7 ms: 1.47x faster                                                        |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 126 ms: 1.38x faster                                                         |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                         |
| regex_effbot   | 3.21 ms                                                | 3.60 ms: 1.12x slower                                                        |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.43x faster                                                        |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                                        |
| pickle               | 10.1 us                                                | 10.3 us: 1.01x slower                                                        |
| pickle_dict          | 28.3 us                                                | 31.0 us: 1.10x slower                                                        |
| pickle_list          | 4.50 us                                                | 4.08 us: 1.10x faster                                                        |
| pickle_pure_python   | 453 us                                                 | 284 us: 1.60x faster                                                         |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                                        |
| unpickle_list        | 4.99 us                                                | 5.07 us: 1.02x slower                                                        |
| unpickle_pure_python | 297 us                                                 | 196 us: 1.51x faster                                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.08x faster                                                         |
| xml_etree_generate   | 93.3 ms                                                | 77.3 ms: 1.21x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.97 ms: 1.55x faster                                                        |
| python_startup_no_site | 5.76 ms                                                | 6.49 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                        |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                        |
| genshi_xml      | 63.6 ms                                                | 46.8 ms: 1.36x faster                                                        |
| mako            | 14.3 ms                                                | 9.56 ms: 1.49x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 250 ms: 1.33x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 990 us: 1.35x faster                                                         |
| async_generators        | 428 ms                                                 | 353 ms: 1.21x faster                                                         |
| async_tree_none         | 713 ms                                                 | 525 ms: 1.36x faster                                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 761 ms: 1.25x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 616 ms: 1.39x faster                                                         |
| chameleon               | 8.86 ms                                                | 6.37 ms: 1.39x faster                                                        |
| chaos                   | 104 ms                                                 | 64.7 ms: 1.61x faster                                                        |
| bench_thread_pool       | 943 us                                                 | 773 us: 1.22x faster                                                         |
| coroutines              | 31.7 ms                                                | 25.3 ms: 1.25x faster                                                        |
| coverage                | 75.3 ms                                                | 97.1 ms: 1.29x slower                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.0 ms: 1.61x faster                                                        |
| deepcopy                | 429 us                                                 | 325 us: 1.32x faster                                                         |
| deepcopy_reduce         | 3.75 us                                                | 2.94 us: 1.28x faster                                                        |
| deepcopy_memo           | 50.0 us                                                | 34.2 us: 1.46x faster                                                        |
| deltablue               | 7.39 ms                                                | 3.19 ms: 2.32x faster                                                        |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                        |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                       |
| dulwich_log             | 75.5 ms                                                | 62.3 ms: 1.21x faster                                                        |
| fannkuch                | 477 ms                                                 | 382 ms: 1.25x faster                                                         |
| float                   | 108 ms                                                 | 72.8 ms: 1.48x faster                                                        |
| generators              | 75.8 ms                                                | 76.8 ms: 1.01x slower                                                        |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                        |
| genshi_xml              | 63.6 ms                                                | 46.8 ms: 1.36x faster                                                        |
| go                      | 226 ms                                                 | 178 ms: 1.27x faster                                                         |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                        |
| hexiom                  | 9.42 ms                                                | 5.99 ms: 1.57x faster                                                        |
| html5lib                | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                        |
| json                    | 5.35 ms                                                | 4.56 ms: 1.17x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.43x faster                                                        |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                                        |
| logging_format          | 8.92 us                                                | 6.20 us: 1.44x faster                                                        |
| logging_silent          | 173 ns                                                 | 92.1 ns: 1.88x faster                                                        |
| logging_simple          | 8.06 us                                                | 5.65 us: 1.42x faster                                                        |
| mako                    | 14.3 ms                                                | 9.56 ms: 1.49x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                                       |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                         |
| mypy                    | 1.01 sec                                               | 806 ms: 1.26x faster                                                         |
| nbody                   | 136 ms                                                 | 92.7 ms: 1.47x faster                                                        |
| nqueens                 | 99.3 ms                                                | 78.6 ms: 1.26x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                        |
| pickle                  | 10.1 us                                                | 10.3 us: 1.01x slower                                                        |
| pickle_dict             | 28.3 us                                                | 31.0 us: 1.10x slower                                                        |
| pickle_list             | 4.50 us                                                | 4.08 us: 1.10x faster                                                        |
| pickle_pure_python      | 453 us                                                 | 284 us: 1.60x faster                                                         |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| pprint_safe_repr        | 943 ms                                                 | 671 ms: 1.40x faster                                                         |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                       |
| pycparser               | 1.51 sec                                               | 1.12 sec: 1.35x faster                                                       |
| pyflate                 | 675 ms                                                 | 405 ms: 1.67x faster                                                         |
| python_startup          | 13.9 ms                                                | 8.97 ms: 1.55x faster                                                        |
| python_startup_no_site  | 5.76 ms                                                | 6.49 ms: 1.13x slower                                                        |
| raytrace                | 461 ms                                                 | 286 ms: 1.61x faster                                                         |
| regex_compile           | 174 ms                                                 | 126 ms: 1.38x faster                                                         |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                         |
| regex_effbot            | 3.21 ms                                                | 3.60 ms: 1.12x slower                                                        |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                        |
| richards                | 71.4 ms                                                | 43.1 ms: 1.65x faster                                                        |
| scimark_fft             | 414 ms                                                 | 303 ms: 1.37x faster                                                         |
| scimark_lu              | 158 ms                                                 | 105 ms: 1.50x faster                                                         |
| scimark_monte_carlo     | 105 ms                                                 | 65.5 ms: 1.60x faster                                                        |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.84x faster                                                         |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.06 ms: 1.35x faster                                                        |
| spectral_norm           | 148 ms                                                 | 99.2 ms: 1.49x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                         |
| sqlite_synth            | 2.90 us                                                | 2.61 us: 1.11x faster                                                        |
| sympy_expand            | 537 ms                                                 | 449 ms: 1.20x faster                                                         |
| sympy_integrate         | 23.9 ms                                                | 19.6 ms: 1.22x faster                                                        |
| sympy_sum               | 183 ms                                                 | 154 ms: 1.19x faster                                                         |
| sympy_str               | 324 ms                                                 | 268 ms: 1.21x faster                                                         |
| telco                   | 6.68 ms                                                | 6.41 ms: 1.04x faster                                                        |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                         |
| tornado_http            | 128 ms                                                 | 94.0 ms: 1.37x faster                                                        |
| unpack_sequence         | 59.5 ns                                                | 41.7 ns: 1.43x faster                                                        |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                                        |
| unpickle_list           | 4.99 us                                                | 5.07 us: 1.02x slower                                                        |
| unpickle_pure_python    | 297 us                                                 | 196 us: 1.51x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.08x faster                                                         |
| xml_etree_generate      | 93.3 ms                                                | 77.3 ms: 1.21x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-d5db69f/bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
