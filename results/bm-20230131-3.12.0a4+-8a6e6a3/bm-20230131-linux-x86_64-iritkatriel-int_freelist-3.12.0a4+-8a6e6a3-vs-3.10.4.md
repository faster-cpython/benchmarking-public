
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 8a6e6a3
- commit date: 2023-01-31
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.37 ms: 1.39x faster                                               |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.8 ms                                                | 61.6 ms: 1.39x faster                                               |
| tornado_http   | 128 ms                                                 | 95.3 ms: 1.35x faster                                               |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.8 ms: 1.46x faster                                               |
| nbody          | 136 ms                                                 | 96.3 ms: 1.41x faster                                               |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 127 ms: 1.37x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                |
| regex_effbot   | 3.21 ms                                                | 3.47 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 286 us: 1.58x faster                                                |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.50 ms: 1.42x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 77.4 ms: 1.20x faster                                               |
| json_loads           | 28.9 us                                                | 24.7 us: 1.17x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| pickle_list          | 4.50 us                                                | 4.23 us: 1.06x faster                                               |
| unpickle             | 14.3 us                                                | 14.0 us: 1.02x faster                                               |
| unpickle_list        | 4.99 us                                                | 4.93 us: 1.01x faster                                               |
| pickle_dict          | 28.3 us                                                | 31.8 us: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.97 ms: 1.55x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.49 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                               |
| mako            | 14.3 ms                                                | 9.80 ms: 1.45x faster                                               |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| genshi_xml      | 63.6 ms                                                | 47.4 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.25 ms: 2.28x faster                                               |
| logging_silent          | 173 ns                                                 | 92.4 ns: 1.87x faster                                               |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                |
| richards                | 71.4 ms                                                | 43.2 ms: 1.65x faster                                               |
| chaos                   | 104 ms                                                 | 64.4 ms: 1.62x faster                                               |
| raytrace                | 461 ms                                                 | 291 ms: 1.59x faster                                                |
| pickle_pure_python      | 453 us                                                 | 286 us: 1.58x faster                                                |
| scimark_monte_carlo     | 105 ms                                                 | 66.4 ms: 1.58x faster                                               |
| hexiom                  | 9.42 ms                                                | 5.98 ms: 1.57x faster                                               |
| scimark_sor             | 193 ms                                                 | 123 ms: 1.57x faster                                                |
| python_startup          | 13.9 ms                                                | 8.97 ms: 1.55x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                               |
| pyflate                 | 675 ms                                                 | 461 ms: 1.46x faster                                                |
| float                   | 108 ms                                                 | 73.8 ms: 1.46x faster                                               |
| mako                    | 14.3 ms                                                | 9.80 ms: 1.45x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                              |
| deepcopy_memo           | 50.0 us                                                | 34.9 us: 1.43x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.50 ms: 1.42x faster                                               |
| nbody                   | 136 ms                                                 | 96.3 ms: 1.41x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 669 ms: 1.41x faster                                                |
| logging_format          | 8.92 us                                                | 6.35 us: 1.41x faster                                               |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| unpack_sequence         | 59.5 ns                                                | 42.7 ns: 1.39x faster                                               |
| html5lib                | 85.8 ms                                                | 61.6 ms: 1.39x faster                                               |
| chameleon               | 8.86 ms                                                | 6.37 ms: 1.39x faster                                               |
| logging_simple          | 8.06 us                                                | 5.79 us: 1.39x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.48 ms: 1.38x faster                                               |
| thrift                  | 1.03 ms                                                | 751 us: 1.37x faster                                                |
| regex_compile           | 174 ms                                                 | 127 ms: 1.37x faster                                                |
| sqlglot_transpile       | 2.42 ms                                                | 1.78 ms: 1.36x faster                                               |
| pycparser               | 1.51 sec                                               | 1.12 sec: 1.35x faster                                              |
| async_tree_none         | 713 ms                                                 | 528 ms: 1.35x faster                                                |
| tornado_http            | 128 ms                                                 | 95.3 ms: 1.35x faster                                               |
| genshi_xml              | 63.6 ms                                                | 47.4 ms: 1.34x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                              |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                               |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                               |
| fannkuch                | 477 ms                                                 | 360 ms: 1.33x faster                                                |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 90.0 ms: 1.31x faster                                               |
| nqueens                 | 99.3 ms                                                | 76.2 ms: 1.30x faster                                               |
| deepcopy                | 429 us                                                 | 331 us: 1.30x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                               |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| mypy                    | 1.01 sec                                               | 805 ms: 1.26x faster                                                |
| coroutines              | 31.7 ms                                                | 25.3 ms: 1.25x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 761 ms: 1.25x faster                                                |
| deepcopy_reduce         | 3.75 us                                                | 3.02 us: 1.24x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.22x faster                                               |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.55 ms: 1.20x faster                                               |
| xml_etree_generate      | 93.3 ms                                                | 77.4 ms: 1.20x faster                                               |
| sympy_str               | 324 ms                                                 | 271 ms: 1.20x faster                                                |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| bench_thread_pool       | 943 us                                                 | 801 us: 1.18x faster                                                |
| dulwich_log             | 75.5 ms                                                | 64.4 ms: 1.17x faster                                               |
| sympy_expand            | 537 ms                                                 | 459 ms: 1.17x faster                                                |
| json_loads              | 28.9 us                                                | 24.7 us: 1.17x faster                                               |
| async_generators        | 428 ms                                                 | 369 ms: 1.16x faster                                                |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                               |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.12x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                |
| sqlite_synth            | 2.90 us                                                | 2.68 us: 1.08x faster                                               |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| spectral_norm           | 148 ms                                                 | 138 ms: 1.07x faster                                                |
| pickle_list             | 4.50 us                                                | 4.23 us: 1.06x faster                                               |
| scimark_fft             | 414 ms                                                 | 390 ms: 1.06x faster                                                |
| pathlib                 | 20.0 ms                                                | 18.9 ms: 1.06x faster                                               |
| telco                   | 6.68 ms                                                | 6.43 ms: 1.04x faster                                               |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                |
| unpickle                | 14.3 us                                                | 14.0 us: 1.02x faster                                               |
| unpickle_list           | 4.99 us                                                | 4.93 us: 1.01x faster                                               |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| regex_effbot            | 3.21 ms                                                | 3.47 ms: 1.08x slower                                               |
| generators              | 75.8 ms                                                | 83.5 ms: 1.10x slower                                               |
| pickle_dict             | 28.3 us                                                | 31.8 us: 1.12x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.49 ms: 1.13x slower                                               |
| coverage                | 75.3 ms                                                | 96.1 ms: 1.28x slower                                               |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                        |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230131-3.12.0a4+-8a6e6a3/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
