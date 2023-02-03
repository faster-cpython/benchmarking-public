
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1d81198
- commit date: 2023-02-03
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.28 ms: 1.41x faster                                               |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                              |
| html5lib       | 85.8 ms                                                | 60.0 ms: 1.43x faster                                               |
| tornado_http   | 128 ms                                                 | 93.7 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.2 ms: 1.47x faster                                               |
| nbody          | 136 ms                                                 | 95.8 ms: 1.42x faster                                               |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.28x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.35x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                |
| regex_effbot   | 3.21 ms                                                | 3.51 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 286 us: 1.59x faster                                                |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.43x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.39x faster                                               |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 77.4 ms: 1.21x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                                |
| unpickle             | 14.3 us                                                | 12.9 us: 1.10x faster                                               |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| pickle_list          | 4.50 us                                                | 4.23 us: 1.06x faster                                               |
| unpickle_list        | 4.99 us                                                | 5.05 us: 1.01x slower                                               |
| pickle_dict          | 28.3 us                                                | 31.3 us: 1.10x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.93 ms: 1.56x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.47 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                               |
| mako            | 14.3 ms                                                | 9.60 ms: 1.48x faster                                               |
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                               |
| genshi_xml      | 63.6 ms                                                | 47.3 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.22 ms: 2.29x faster                                               |
| logging_silent          | 173 ns                                                 | 91.9 ns: 1.88x faster                                               |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                |
| richards                | 71.4 ms                                                | 42.0 ms: 1.70x faster                                               |
| go                      | 226 ms                                                 | 135 ms: 1.68x faster                                                |
| chaos                   | 104 ms                                                 | 63.7 ms: 1.63x faster                                               |
| pyflate                 | 675 ms                                                 | 416 ms: 1.62x faster                                                |
| raytrace                | 461 ms                                                 | 289 ms: 1.59x faster                                                |
| pickle_pure_python      | 453 us                                                 | 286 us: 1.59x faster                                                |
| hexiom                  | 9.42 ms                                                | 5.96 ms: 1.58x faster                                               |
| scimark_monte_carlo     | 105 ms                                                 | 66.8 ms: 1.57x faster                                               |
| python_startup          | 13.9 ms                                                | 8.93 ms: 1.56x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.0 ms: 1.55x faster                                               |
| spectral_norm           | 148 ms                                                 | 98.2 ms: 1.51x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                |
| mako                    | 14.3 ms                                                | 9.60 ms: 1.48x faster                                               |
| float                   | 108 ms                                                 | 73.2 ms: 1.47x faster                                               |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.47x faster                                                |
| deepcopy_memo           | 50.0 us                                                | 34.2 us: 1.46x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                              |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.43x faster                                               |
| html5lib                | 85.8 ms                                                | 60.0 ms: 1.43x faster                                               |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                               |
| nbody                   | 136 ms                                                 | 95.8 ms: 1.42x faster                                               |
| logging_format          | 8.92 us                                                | 6.32 us: 1.41x faster                                               |
| chameleon               | 8.86 ms                                                | 6.28 ms: 1.41x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 671 ms: 1.40x faster                                                |
| logging_simple          | 8.06 us                                                | 5.73 us: 1.40x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.39x faster                                               |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                                |
| tornado_http            | 128 ms                                                 | 93.7 ms: 1.37x faster                                               |
| async_tree_none         | 713 ms                                                 | 522 ms: 1.37x faster                                                |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.02 ms: 1.36x faster                                               |
| regex_compile           | 174 ms                                                 | 128 ms: 1.35x faster                                                |
| unpack_sequence         | 59.5 ns                                                | 43.9 ns: 1.35x faster                                               |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                               |
| aiohttp                 | 1.34 ms                                                | 993 us: 1.35x faster                                                |
| genshi_xml              | 63.6 ms                                                | 47.3 ms: 1.34x faster                                               |
| scimark_fft             | 414 ms                                                 | 308 ms: 1.34x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                              |
| pycparser               | 1.51 sec                                               | 1.13 sec: 1.33x faster                                              |
| async_tree_memoization  | 854 ms                                                 | 647 ms: 1.32x faster                                                |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| nqueens                 | 99.3 ms                                                | 75.7 ms: 1.31x faster                                               |
| coroutines              | 31.7 ms                                                | 24.3 ms: 1.30x faster                                               |
| deepcopy                | 429 us                                                 | 330 us: 1.30x faster                                                |
| fannkuch                | 477 ms                                                 | 369 ms: 1.29x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                |
| deepcopy_reduce         | 3.75 us                                                | 2.96 us: 1.27x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 753 ms: 1.26x faster                                                |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                |
| dulwich_log             | 75.5 ms                                                | 62.3 ms: 1.21x faster                                               |
| async_generators        | 428 ms                                                 | 354 ms: 1.21x faster                                                |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                               |
| xml_etree_generate      | 93.3 ms                                                | 77.4 ms: 1.21x faster                                               |
| bench_thread_pool       | 943 us                                                 | 782 us: 1.21x faster                                                |
| sympy_str               | 324 ms                                                 | 271 ms: 1.20x faster                                                |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.17x faster                                                |
| sqlite_synth            | 2.90 us                                                | 2.54 us: 1.14x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                               |
| json                    | 5.35 ms                                                | 4.76 ms: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                                |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| unpickle                | 14.3 us                                                | 12.9 us: 1.10x faster                                               |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                              |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| pickle_list             | 4.50 us                                                | 4.23 us: 1.06x faster                                               |
| telco                   | 6.68 ms                                                | 6.37 ms: 1.05x faster                                               |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| unpickle_list           | 4.99 us                                                | 5.05 us: 1.01x slower                                               |
| generators              | 75.8 ms                                                | 77.1 ms: 1.02x slower                                               |
| regex_effbot            | 3.21 ms                                                | 3.51 ms: 1.10x slower                                               |
| pickle_dict             | 28.3 us                                                | 31.3 us: 1.10x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.47 ms: 1.12x slower                                               |
| coverage                | 75.3 ms                                                | 96.4 ms: 1.28x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-1d81198/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
