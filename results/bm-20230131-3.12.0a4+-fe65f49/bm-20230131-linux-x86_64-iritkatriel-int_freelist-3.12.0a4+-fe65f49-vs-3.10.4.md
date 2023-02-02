
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: fe65f49
- commit date: 2023-01-31
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.36 ms: 1.39x faster                                               |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                              |
| html5lib       | 85.8 ms                                                | 61.1 ms: 1.40x faster                                               |
| tornado_http   | 128 ms                                                 | 94.6 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.8 ms: 1.46x faster                                               |
| nbody          | 136 ms                                                 | 98.3 ms: 1.39x faster                                               |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                |
| regex_effbot   | 3.21 ms                                                | 3.54 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.47 ms: 1.42x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 77.4 ms: 1.21x faster                                               |
| json_loads           | 28.9 us                                                | 25.1 us: 1.15x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| unpickle             | 14.3 us                                                | 13.3 us: 1.08x faster                                               |
| pickle_list          | 4.50 us                                                | 4.18 us: 1.08x faster                                               |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| unpickle_list        | 4.99 us                                                | 4.93 us: 1.01x faster                                               |
| pickle_dict          | 28.3 us                                                | 31.6 us: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.96 ms: 1.56x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.47 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.50x faster                                               |
| mako            | 14.3 ms                                                | 9.78 ms: 1.46x faster                                               |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                               |
| genshi_xml      | 63.6 ms                                                | 47.2 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.25 ms: 2.28x faster                                               |
| logging_silent          | 173 ns                                                 | 91.8 ns: 1.89x faster                                               |
| richards                | 71.4 ms                                                | 42.9 ms: 1.66x faster                                               |
| go                      | 226 ms                                                 | 141 ms: 1.61x faster                                                |
| raytrace                | 461 ms                                                 | 288 ms: 1.60x faster                                                |
| pickle_pure_python      | 453 us                                                 | 287 us: 1.58x faster                                                |
| hexiom                  | 9.42 ms                                                | 6.03 ms: 1.56x faster                                               |
| chaos                   | 104 ms                                                 | 66.9 ms: 1.56x faster                                               |
| python_startup          | 13.9 ms                                                | 8.96 ms: 1.56x faster                                               |
| scimark_sor             | 193 ms                                                 | 125 ms: 1.55x faster                                                |
| scimark_monte_carlo     | 105 ms                                                 | 68.3 ms: 1.53x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.50x faster                                               |
| float                   | 108 ms                                                 | 73.8 ms: 1.46x faster                                               |
| pyflate                 | 675 ms                                                 | 463 ms: 1.46x faster                                                |
| mako                    | 14.3 ms                                                | 9.78 ms: 1.46x faster                                               |
| scimark_lu              | 158 ms                                                 | 109 ms: 1.45x faster                                                |
| deepcopy_memo           | 50.0 us                                                | 34.6 us: 1.44x faster                                               |
| logging_format          | 8.92 us                                                | 6.23 us: 1.43x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                              |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.47 ms: 1.42x faster                                               |
| logging_simple          | 8.06 us                                                | 5.67 us: 1.42x faster                                               |
| thrift                  | 1.03 ms                                                | 731 us: 1.41x faster                                                |
| html5lib                | 85.8 ms                                                | 61.1 ms: 1.40x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                                |
| unpack_sequence         | 59.5 ns                                                | 42.6 ns: 1.40x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.46 ms: 1.39x faster                                               |
| chameleon               | 8.86 ms                                                | 6.36 ms: 1.39x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                               |
| nbody                   | 136 ms                                                 | 98.3 ms: 1.39x faster                                               |
| sqlglot_transpile       | 2.42 ms                                                | 1.76 ms: 1.37x faster                                               |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                |
| tornado_http            | 128 ms                                                 | 94.6 ms: 1.36x faster                                               |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| genshi_xml              | 63.6 ms                                                | 47.2 ms: 1.35x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 635 ms: 1.35x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                               |
| aiohttp                 | 1.34 ms                                                | 1000 us: 1.34x faster                                               |
| deepcopy                | 429 us                                                 | 325 us: 1.32x faster                                                |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| fannkuch                | 477 ms                                                 | 362 ms: 1.32x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 89.3 ms: 1.32x faster                                               |
| pycparser               | 1.51 sec                                               | 1.17 sec: 1.30x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                               |
| nqueens                 | 99.3 ms                                                | 77.9 ms: 1.28x faster                                               |
| deepcopy_reduce         | 3.75 us                                                | 2.95 us: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                              |
| coroutines              | 31.7 ms                                                | 25.1 ms: 1.26x faster                                               |
| mypy                    | 1.01 sec                                               | 804 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                                |
| sympy_integrate         | 23.9 ms                                                | 19.6 ms: 1.22x faster                                               |
| xml_etree_generate      | 93.3 ms                                                | 77.4 ms: 1.21x faster                                               |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                |
| sympy_sum               | 183 ms                                                 | 154 ms: 1.19x faster                                                |
| sympy_expand            | 537 ms                                                 | 454 ms: 1.18x faster                                                |
| bench_thread_pool       | 943 us                                                 | 800 us: 1.18x faster                                                |
| dulwich_log             | 75.5 ms                                                | 64.6 ms: 1.17x faster                                               |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.71 ms: 1.16x faster                                               |
| json_loads              | 28.9 us                                                | 25.1 us: 1.15x faster                                               |
| async_generators        | 428 ms                                                 | 373 ms: 1.15x faster                                                |
| json                    | 5.35 ms                                                | 4.73 ms: 1.13x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                              |
| sqlite_synth            | 2.90 us                                                | 2.68 us: 1.08x faster                                               |
| unpickle                | 14.3 us                                                | 13.3 us: 1.08x faster                                               |
| pickle_list             | 4.50 us                                                | 4.18 us: 1.08x faster                                               |
| spectral_norm           | 148 ms                                                 | 138 ms: 1.07x faster                                                |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| pathlib                 | 20.0 ms                                                | 19.1 ms: 1.05x faster                                               |
| telco                   | 6.68 ms                                                | 6.37 ms: 1.05x faster                                               |
| scimark_fft             | 414 ms                                                 | 399 ms: 1.04x faster                                                |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                |
| unpickle_list           | 4.99 us                                                | 4.93 us: 1.01x faster                                               |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| generators              | 75.8 ms                                                | 79.5 ms: 1.05x slower                                               |
| regex_effbot            | 3.21 ms                                                | 3.54 ms: 1.10x slower                                               |
| pickle_dict             | 28.3 us                                                | 31.6 us: 1.12x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.47 ms: 1.12x slower                                               |
| coverage                | 75.3 ms                                                | 98.2 ms: 1.30x slower                                               |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                        |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230131-3.12.0a4+-fe65f49/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
