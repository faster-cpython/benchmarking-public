
# Results vs. 3.10.4

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 96e2742
- commit date: 2023-02-08
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                               |
| chameleon      | 8.86 ms                                                | 6.48 ms: 1.37x faster                                              |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                             |
| html5lib       | 85.8 ms                                                | 60.8 ms: 1.41x faster                                              |
| tornado_http   | 128 ms                                                 | 94.1 ms: 1.36x faster                                              |
| Geometric mean | (ref)                                                  | 1.34x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 136 ms                                                 | 86.6 ms: 1.57x faster                                              |
| float          | 108 ms                                                 | 71.8 ms: 1.50x faster                                              |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                               |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                              |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                               |
| regex_effbot   | 3.21 ms                                                | 3.40 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 289 us: 1.57x faster                                               |
| unpickle_pure_python | 297 us                                                 | 199 us: 1.49x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                              |
| xml_etree_process    | 74.5 ms                                                | 55.4 ms: 1.34x faster                                              |
| json_loads           | 28.9 us                                                | 23.8 us: 1.21x faster                                              |
| xml_etree_generate   | 93.3 ms                                                | 80.0 ms: 1.17x faster                                              |
| pickle_list          | 4.50 us                                                | 4.03 us: 1.12x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                              |
| xml_etree_iterparse  | 110 ms                                                 | 107 ms: 1.03x faster                                               |
| pickle_dict          | 28.3 us                                                | 31.0 us: 1.10x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.90 ms: 1.57x faster                                              |
| python_startup_no_site | 5.76 ms                                                | 6.45 ms: 1.12x slower                                              |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                              |
| mako            | 14.3 ms                                                | 9.64 ms: 1.48x faster                                              |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                              |
| genshi_xml      | 63.6 ms                                                | 46.3 ms: 1.37x faster                                              |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.19 ms: 2.32x faster                                              |
| logging_silent          | 173 ns                                                 | 93.6 ns: 1.85x faster                                              |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                               |
| richards                | 71.4 ms                                                | 42.6 ms: 1.68x faster                                              |
| pyflate                 | 675 ms                                                 | 403 ms: 1.67x faster                                               |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                               |
| raytrace                | 461 ms                                                 | 282 ms: 1.64x faster                                               |
| chaos                   | 104 ms                                                 | 64.3 ms: 1.62x faster                                              |
| crypto_pyaes            | 118 ms                                                 | 73.0 ms: 1.61x faster                                              |
| scimark_monte_carlo     | 105 ms                                                 | 65.8 ms: 1.59x faster                                              |
| nbody                   | 136 ms                                                 | 86.6 ms: 1.57x faster                                              |
| pickle_pure_python      | 453 us                                                 | 289 us: 1.57x faster                                               |
| spectral_norm           | 148 ms                                                 | 94.3 ms: 1.57x faster                                              |
| hexiom                  | 9.42 ms                                                | 6.00 ms: 1.57x faster                                              |
| python_startup          | 13.9 ms                                                | 8.90 ms: 1.57x faster                                              |
| float                   | 108 ms                                                 | 71.8 ms: 1.50x faster                                              |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                              |
| unpickle_pure_python    | 297 us                                                 | 199 us: 1.49x faster                                               |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.49x faster                                               |
| mako                    | 14.3 ms                                                | 9.64 ms: 1.48x faster                                              |
| deepcopy_memo           | 50.0 us                                                | 34.3 us: 1.46x faster                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                              |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                             |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                              |
| logging_format          | 8.92 us                                                | 6.27 us: 1.42x faster                                              |
| html5lib                | 85.8 ms                                                | 60.8 ms: 1.41x faster                                              |
| sqlglot_transpile       | 2.42 ms                                                | 1.72 ms: 1.41x faster                                              |
| logging_simple          | 8.06 us                                                | 5.74 us: 1.40x faster                                              |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.91 ms: 1.40x faster                                              |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                               |
| scimark_fft             | 414 ms                                                 | 298 ms: 1.39x faster                                               |
| pycparser               | 1.51 sec                                               | 1.10 sec: 1.38x faster                                             |
| genshi_xml              | 63.6 ms                                                | 46.3 ms: 1.37x faster                                              |
| chameleon               | 8.86 ms                                                | 6.48 ms: 1.37x faster                                              |
| thrift                  | 1.03 ms                                                | 756 us: 1.37x faster                                               |
| tornado_http            | 128 ms                                                 | 94.1 ms: 1.36x faster                                              |
| async_tree_none         | 713 ms                                                 | 523 ms: 1.36x faster                                               |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                             |
| xml_etree_process       | 74.5 ms                                                | 55.4 ms: 1.34x faster                                              |
| unpack_sequence         | 59.5 ns                                                | 44.6 ns: 1.33x faster                                              |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                              |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                              |
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                               |
| deepcopy                | 429 us                                                 | 327 us: 1.31x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 652 ms: 1.31x faster                                               |
| deepcopy_reduce         | 3.75 us                                                | 2.89 us: 1.30x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 751 ms: 1.26x faster                                               |
| nqueens                 | 99.3 ms                                                | 78.9 ms: 1.26x faster                                              |
| coroutines              | 31.7 ms                                                | 25.2 ms: 1.26x faster                                              |
| fannkuch                | 477 ms                                                 | 382 ms: 1.25x faster                                               |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                             |
| json_loads              | 28.9 us                                                | 23.8 us: 1.21x faster                                              |
| sympy_integrate         | 23.9 ms                                                | 19.9 ms: 1.20x faster                                              |
| bench_thread_pool       | 943 us                                                 | 784 us: 1.20x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                               |
| dulwich_log             | 75.5 ms                                                | 62.9 ms: 1.20x faster                                              |
| sympy_str               | 324 ms                                                 | 271 ms: 1.20x faster                                               |
| sympy_expand            | 537 ms                                                 | 455 ms: 1.18x faster                                               |
| json                    | 5.35 ms                                                | 4.56 ms: 1.17x faster                                              |
| xml_etree_generate      | 93.3 ms                                                | 80.0 ms: 1.17x faster                                              |
| sqlalchemy_imperative   | 21.0 ms                                                | 18.1 ms: 1.16x faster                                              |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                              |
| sqlite_synth            | 2.90 us                                                | 2.55 us: 1.14x faster                                              |
| pickle_list             | 4.50 us                                                | 4.03 us: 1.12x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                              |
| mdp                     | 2.82 sec                                               | 2.66 sec: 1.06x faster                                             |
| meteor_contest          | 114 ms                                                 | 108 ms: 1.05x faster                                               |
| telco                   | 6.68 ms                                                | 6.47 ms: 1.03x faster                                              |
| xml_etree_iterparse     | 110 ms                                                 | 107 ms: 1.03x faster                                               |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                               |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                               |
| async_generators        | 428 ms                                                 | 431 ms: 1.01x slower                                               |
| generators              | 75.8 ms                                                | 78.2 ms: 1.03x slower                                              |
| regex_effbot            | 3.21 ms                                                | 3.40 ms: 1.06x slower                                              |
| pickle_dict             | 28.3 us                                                | 31.0 us: 1.10x slower                                              |
| python_startup_no_site  | 5.76 ms                                                | 6.45 ms: 1.12x slower                                              |
| coverage                | 75.3 ms                                                | 96.9 ms: 1.29x slower                                              |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                       |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, pickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230208-3.12.0a5+-96e2742/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
