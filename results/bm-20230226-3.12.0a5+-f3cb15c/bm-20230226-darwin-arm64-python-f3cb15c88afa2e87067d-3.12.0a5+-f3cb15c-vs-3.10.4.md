
# Results vs. 3.10.4

- fork: python
- ref: f3cb15c88afa2e87067d
- machine: darwin-arm64
- commit hash: f3cb15c
- commit date: 2023-02-26
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 164 ms: 1.23x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.41 ms: 1.31x faster                                                  |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.20x faster                                                 |
| html5lib       | 44.2 ms                                                | 35.7 ms: 1.24x faster                                                  |
| tornado_http   | 91.5 ms                                                | 71.3 ms: 1.28x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.9 ms: 1.46x faster                                                  |
| float          | 72.4 ms                                                | 53.0 ms: 1.36x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.2 ms: 1.28x faster                                                  |
| regex_v8       | 17.6 ms                                                | 16.0 ms: 1.09x faster                                                  |
| regex_dna      | 162 ms                                                 | 152 ms: 1.06x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.69 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 195 us: 1.45x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 142 us: 1.43x faster                                                   |
| json_dumps           | 8.40 ms                                                | 6.22 ms: 1.35x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 36.2 ms: 1.24x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 96.7 ms: 1.10x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 50.7 ms: 1.07x faster                                                  |
| json_loads           | 16.9 us                                                | 15.9 us: 1.06x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 70.2 ms: 1.03x faster                                                  |
| unpickle             | 9.89 us                                                | 9.73 us: 1.02x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.1 us: 1.01x slower                                                  |
| pickle               | 7.35 us                                                | 7.54 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.5 ms: 1.05x slower                                                  |
| python_startup_no_site | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.43 ms: 1.41x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 28.4 ms: 1.31x faster                                                  |
| genshi_text     | 18.4 ms                                                | 14.4 ms: 1.28x faster                                                  |
| django_template | 27.3 ms                                                | 21.4 ms: 1.28x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-darwin-arm64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.56 ms: 2.01x faster                                                  |
| logging_silent          | 119 ns                                                 | 66.9 ns: 1.78x faster                                                  |
| richards                | 51.4 ms                                                | 30.4 ms: 1.69x faster                                                  |
| go                      | 165 ms                                                 | 109 ms: 1.51x faster                                                   |
| asyncio_tcp             | 670 ms                                                 | 448 ms: 1.49x faster                                                   |
| scimark_lu              | 109 ms                                                 | 73.5 ms: 1.49x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 335 ms: 1.47x faster                                                   |
| nbody                   | 93.3 ms                                                | 63.9 ms: 1.46x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 53.6 ms: 1.46x faster                                                  |
| raytrace                | 325 ms                                                 | 223 ms: 1.46x faster                                                   |
| pickle_pure_python      | 283 us                                                 | 195 us: 1.45x faster                                                   |
| scimark_sor             | 126 ms                                                 | 86.7 ms: 1.45x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.35 ms: 1.45x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 142 us: 1.43x faster                                                   |
| mako                    | 10.5 ms                                                | 7.43 ms: 1.41x faster                                                  |
| chaos                   | 66.7 ms                                                | 47.6 ms: 1.40x faster                                                  |
| async_tree_none         | 400 ms                                                 | 288 ms: 1.39x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 738 ms: 1.38x faster                                                   |
| pyflate                 | 453 ms                                                 | 328 ms: 1.38x faster                                                   |
| pycparser               | 916 ms                                                 | 668 ms: 1.37x faster                                                   |
| float                   | 72.4 ms                                                | 53.0 ms: 1.36x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 53.2 ms: 1.36x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.22 ms: 1.35x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 25.7 us: 1.34x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.41 ms: 1.31x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 28.4 ms: 1.31x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.06 ms: 1.28x faster                                                  |
| generators              | 32.7 ms                                                | 25.5 ms: 1.28x faster                                                  |
| tornado_http            | 91.5 ms                                                | 71.3 ms: 1.28x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.61 us: 1.28x faster                                                  |
| regex_compile           | 96.4 ms                                                | 75.2 ms: 1.28x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 473 ms: 1.28x faster                                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.23 ms: 1.28x faster                                                  |
| thrift                  | 580 us                                                 | 454 us: 1.28x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 964 ms: 1.28x faster                                                   |
| genshi_text             | 18.4 ms                                                | 14.4 ms: 1.28x faster                                                  |
| django_template         | 27.3 ms                                                | 21.4 ms: 1.28x faster                                                  |
| logging_format          | 4.97 us                                                | 3.91 us: 1.27x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 75.5 ms: 1.27x faster                                                  |
| deepcopy                | 281 us                                                 | 222 us: 1.27x faster                                                   |
| create_gc_cycles        | 880 us                                                 | 702 us: 1.25x faster                                                   |
| dulwich_log             | 37.1 ms                                                | 29.6 ms: 1.25x faster                                                  |
| fannkuch                | 317 ms                                                 | 255 ms: 1.24x faster                                                   |
| html5lib                | 44.2 ms                                                | 35.7 ms: 1.24x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 36.2 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 542 ms: 1.23x faster                                                   |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.22 ms: 1.23x faster                                                  |
| 2to3                    | 201 ms                                                 | 164 ms: 1.23x faster                                                   |
| deepcopy_reduce         | 2.37 us                                                | 1.95 us: 1.22x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 31.7 ms: 1.20x faster                                                  |
| docutils                | 1.78 sec                                               | 1.49 sec: 1.20x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 63.8 ms: 1.17x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 466 us: 1.17x faster                                                   |
| scimark_fft             | 230 ms                                                 | 197 ms: 1.17x faster                                                   |
| mypy2                   | 307 ms                                                 | 263 ms: 1.17x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.6 ms: 1.14x faster                                                  |
| coroutines              | 20.2 ms                                                | 17.7 ms: 1.14x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 173 ms: 1.13x faster                                                   |
| unpack_sequence         | 37.4 ns                                                | 33.2 ns: 1.13x faster                                                  |
| sympy_expand            | 275 ms                                                 | 245 ms: 1.12x faster                                                   |
| json                    | 3.08 ms                                                | 2.78 ms: 1.11x faster                                                  |
| nqueens                 | 68.2 ms                                                | 61.9 ms: 1.10x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 96.7 ms: 1.10x faster                                                  |
| sympy_str               | 169 ms                                                 | 154 ms: 1.10x faster                                                   |
| regex_v8                | 17.6 ms                                                | 16.0 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.19 ms: 1.08x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.08x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 50.7 ms: 1.07x faster                                                  |
| regex_dna               | 162 ms                                                 | 152 ms: 1.06x faster                                                   |
| sympy_sum               | 93.6 ms                                                | 88.2 ms: 1.06x faster                                                  |
| json_loads              | 16.9 us                                                | 15.9 us: 1.06x faster                                                  |
| pathlib                 | 28.8 ms                                                | 27.2 ms: 1.06x faster                                                  |
| telco                   | 3.63 ms                                                | 3.49 ms: 1.04x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 70.2 ms: 1.03x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 76.1 ms: 1.03x faster                                                  |
| unpickle                | 9.89 us                                                | 9.73 us: 1.02x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| pickle_dict             | 17.9 us                                                | 18.1 us: 1.01x slower                                                  |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.01x slower                                                  |
| pickle                  | 7.35 us                                                | 7.54 us: 1.03x slower                                                  |
| comprehensions          | 17.6 us                                                | 18.2 us: 1.03x slower                                                  |
| python_startup          | 11.9 ms                                                | 12.5 ms: 1.05x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.69 ms: 1.09x slower                                                  |
| async_generators        | 234 ms                                                 | 266 ms: 1.14x slower                                                   |
| bench_mp_pool           | 39.7 ms                                                | 46.3 ms: 1.17x slower                                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                  |
| dask                    | 265 ms                                                 | 323 ms: 1.22x slower                                                   |
| coverage                | 42.0 ms                                                | 60.3 ms: 1.44x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (2): unpickle_list, pickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
