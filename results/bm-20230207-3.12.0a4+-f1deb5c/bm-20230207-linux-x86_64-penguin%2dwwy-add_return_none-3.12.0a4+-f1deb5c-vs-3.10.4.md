
# Results vs. 3.10.4

- fork: penguin-wwy
- ref: add_return_none
- machine: linux-x86_64
- commit hash: f1deb5c
- commit date: 2023-02-07
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.33x faster                                                     |
| chameleon      | 8.86 ms                                                | 6.36 ms: 1.39x faster                                                    |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                   |
| html5lib       | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                    |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.1 ms: 1.49x faster                                                    |
| nbody          | 136 ms                                                 | 95.5 ms: 1.43x faster                                                    |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.27x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 127 ms: 1.37x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                    |
| regex_dna      | 214 ms                                                 | 200 ms: 1.07x faster                                                     |
| regex_effbot   | 3.21 ms                                                | 3.50 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 284 us: 1.60x faster                                                     |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                    |
| xml_etree_generate   | 93.3 ms                                                | 77.1 ms: 1.21x faster                                                    |
| json_loads           | 28.9 us                                                | 24.2 us: 1.19x faster                                                    |
| pickle_list          | 4.50 us                                                | 4.07 us: 1.11x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                     |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                                    |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.08x faster                                                     |
| pickle               | 10.1 us                                                | 9.99 us: 1.01x faster                                                    |
| unpickle_list        | 4.99 us                                                | 5.07 us: 1.02x slower                                                    |
| pickle_dict          | 28.3 us                                                | 30.6 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.90 ms: 1.57x faster                                                    |
| python_startup_no_site | 5.76 ms                                                | 6.46 ms: 1.12x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                    |
| mako            | 14.3 ms                                                | 9.63 ms: 1.48x faster                                                    |
| django_template | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                    |
| genshi_xml      | 63.6 ms                                                | 46.6 ms: 1.36x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.16 ms: 2.34x faster                                                    |
| logging_silent          | 173 ns                                                 | 90.7 ns: 1.91x faster                                                    |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.81x faster                                                     |
| richards                | 71.4 ms                                                | 41.9 ms: 1.70x faster                                                    |
| pyflate                 | 675 ms                                                 | 406 ms: 1.66x faster                                                     |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                                     |
| raytrace                | 461 ms                                                 | 285 ms: 1.62x faster                                                     |
| chaos                   | 104 ms                                                 | 64.6 ms: 1.61x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 73.2 ms: 1.60x faster                                                    |
| scimark_monte_carlo     | 105 ms                                                 | 65.3 ms: 1.60x faster                                                    |
| pickle_pure_python      | 453 us                                                 | 284 us: 1.60x faster                                                     |
| hexiom                  | 9.42 ms                                                | 5.96 ms: 1.58x faster                                                    |
| python_startup          | 13.9 ms                                                | 8.90 ms: 1.57x faster                                                    |
| spectral_norm           | 148 ms                                                 | 94.9 ms: 1.56x faster                                                    |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                     |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                    |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.49x faster                                                     |
| float                   | 108 ms                                                 | 72.1 ms: 1.49x faster                                                    |
| mako                    | 14.3 ms                                                | 9.63 ms: 1.48x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                                    |
| deepcopy_memo           | 50.0 us                                                | 34.5 us: 1.45x faster                                                    |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                                   |
| html5lib                | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                    |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                                    |
| nbody                   | 136 ms                                                 | 95.5 ms: 1.43x faster                                                    |
| logging_format          | 8.92 us                                                | 6.29 us: 1.42x faster                                                    |
| logging_simple          | 8.06 us                                                | 5.69 us: 1.42x faster                                                    |
| pprint_safe_repr        | 943 ms                                                 | 668 ms: 1.41x faster                                                     |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                                     |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                    |
| chameleon               | 8.86 ms                                                | 6.36 ms: 1.39x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                    |
| unpack_sequence         | 59.5 ns                                                | 43.0 ns: 1.38x faster                                                    |
| regex_compile           | 174 ms                                                 | 127 ms: 1.37x faster                                                     |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                                    |
| pycparser               | 1.51 sec                                               | 1.11 sec: 1.37x faster                                                   |
| scimark_fft             | 414 ms                                                 | 303 ms: 1.37x faster                                                     |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.01 ms: 1.37x faster                                                    |
| genshi_xml              | 63.6 ms                                                | 46.6 ms: 1.36x faster                                                    |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                     |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                    |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.34x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                   |
| 2to3                    | 332 ms                                                 | 251 ms: 1.33x faster                                                     |
| deepcopy                | 429 us                                                 | 332 us: 1.29x faster                                                     |
| fannkuch                | 477 ms                                                 | 370 ms: 1.29x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 667 ms: 1.28x faster                                                     |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                    |
| nqueens                 | 99.3 ms                                                | 77.8 ms: 1.28x faster                                                    |
| deepcopy_reduce         | 3.75 us                                                | 2.95 us: 1.27x faster                                                    |
| mypy                    | 1.01 sec                                               | 803 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 754 ms: 1.26x faster                                                     |
| coroutines              | 31.7 ms                                                | 25.3 ms: 1.25x faster                                                    |
| async_generators        | 428 ms                                                 | 349 ms: 1.23x faster                                                     |
| dulwich_log             | 75.5 ms                                                | 62.2 ms: 1.21x faster                                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                     |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                                    |
| xml_etree_generate      | 93.3 ms                                                | 77.1 ms: 1.21x faster                                                    |
| bench_thread_pool       | 943 us                                                 | 780 us: 1.21x faster                                                     |
| sympy_str               | 324 ms                                                 | 269 ms: 1.21x faster                                                     |
| sqlalchemy_imperative   | 21.0 ms                                                | 17.5 ms: 1.20x faster                                                    |
| json_loads              | 28.9 us                                                | 24.2 us: 1.19x faster                                                    |
| sympy_expand            | 537 ms                                                 | 454 ms: 1.18x faster                                                     |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                    |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                    |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.13x faster                                                    |
| pickle_list             | 4.50 us                                                | 4.07 us: 1.11x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                     |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.08x faster                                                   |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.08x faster                                                     |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                                     |
| regex_dna               | 214 ms                                                 | 200 ms: 1.07x faster                                                     |
| telco                   | 6.68 ms                                                | 6.33 ms: 1.06x faster                                                    |
| pickle                  | 10.1 us                                                | 9.99 us: 1.01x faster                                                    |
| generators              | 75.8 ms                                                | 75.6 ms: 1.00x faster                                                    |
| unpickle_list           | 4.99 us                                                | 5.07 us: 1.02x slower                                                    |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                     |
| pickle_dict             | 28.3 us                                                | 30.6 us: 1.08x slower                                                    |
| regex_effbot            | 3.21 ms                                                | 3.50 ms: 1.09x slower                                                    |
| python_startup_no_site  | 5.76 ms                                                | 6.46 ms: 1.12x slower                                                    |
| coverage                | 75.3 ms                                                | 98.4 ms: 1.31x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.12.0a4+-f1deb5c/bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal
