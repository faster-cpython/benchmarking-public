
# Results vs. 3.10.4

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: darwin-arm64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 162 ms: 1.24x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.55 ms: 1.27x faster                                                 |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| html5lib       | 44.2 ms                                                | 33.8 ms: 1.31x faster                                                 |
| tornado_http   | 91.5 ms                                                | 72.3 ms: 1.27x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 66.1 ms: 1.41x faster                                                 |
| float          | 72.4 ms                                                | 52.8 ms: 1.37x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.5 ms: 1.28x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.20 ms: 1.12x faster                                                 |
| regex_dna      | 162 ms                                                 | 171 ms: 1.06x slower                                                  |
| regex_v8       | 17.6 ms                                                | 19.8 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 199 us: 1.42x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 157 us: 1.29x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 35.2 ms: 1.27x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 48.2 ms: 1.12x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.68 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 67.3 ms: 1.07x faster                                                 |
| json_loads           | 16.9 us                                                | 15.9 us: 1.06x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.05x faster                                                  |
| pickle               | 7.35 us                                                | 7.15 us: 1.03x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.6 us: 1.02x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.65 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 9.78 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.2 ms: 1.28x faster                                                 |
| mako            | 10.5 ms                                                | 8.21 ms: 1.28x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 30.5 ms: 1.22x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.1 ms: 1.21x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.69 ms: 1.91x faster                                                 |
| logging_silent          | 119 ns                                                 | 69.6 ns: 1.71x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 45.3 ms: 1.60x faster                                                 |
| richards                | 51.4 ms                                                | 32.6 ms: 1.57x faster                                                 |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                                  |
| scimark_sor             | 126 ms                                                 | 82.2 ms: 1.53x faster                                                 |
| raytrace                | 325 ms                                                 | 212 ms: 1.53x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 323 ms: 1.52x faster                                                  |
| scimark_lu              | 109 ms                                                 | 72.2 ms: 1.51x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 703 ms: 1.45x faster                                                  |
| pyflate                 | 453 ms                                                 | 316 ms: 1.43x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 199 us: 1.42x faster                                                  |
| nbody                   | 93.3 ms                                                | 66.1 ms: 1.41x faster                                                 |
| async_tree_none         | 400 ms                                                 | 283 ms: 1.41x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 56.5 ms: 1.38x faster                                                 |
| float                   | 72.4 ms                                                | 52.8 ms: 1.37x faster                                                 |
| logging_format          | 4.97 us                                                | 3.65 us: 1.36x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.41 us: 1.36x faster                                                 |
| thrift                  | 580 us                                                 | 432 us: 1.34x faster                                                  |
| chaos                   | 66.7 ms                                                | 49.7 ms: 1.34x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 25.8 us: 1.33x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 457 ms: 1.32x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 937 ms: 1.31x faster                                                  |
| html5lib                | 44.2 ms                                                | 33.8 ms: 1.31x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 73.4 ms: 1.31x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.88 ms: 1.29x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 157 us: 1.29x faster                                                  |
| django_template         | 27.3 ms                                                | 21.2 ms: 1.28x faster                                                 |
| mako                    | 10.5 ms                                                | 8.21 ms: 1.28x faster                                                 |
| pycparser               | 916 ms                                                 | 717 ms: 1.28x faster                                                  |
| regex_compile           | 96.4 ms                                                | 75.5 ms: 1.28x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.55 ms: 1.27x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 35.2 ms: 1.27x faster                                                 |
| tornado_http            | 91.5 ms                                                | 72.3 ms: 1.27x faster                                                 |
| 2to3                    | 201 ms                                                 | 162 ms: 1.24x faster                                                  |
| deepcopy                | 281 us                                                 | 227 us: 1.24x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 541 ms: 1.24x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.93 us: 1.23x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 30.3 ms: 1.22x faster                                                 |
| dask                    | 265 ms                                                 | 217 ms: 1.22x faster                                                  |
| mypy2                   | 307 ms                                                 | 251 ms: 1.22x faster                                                  |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| genshi_xml              | 37.2 ms                                                | 30.5 ms: 1.22x faster                                                 |
| create_gc_cycles        | 880 us                                                 | 724 us: 1.21x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.1 ms: 1.21x faster                                                 |
| async_generators        | 234 ms                                                 | 193 ms: 1.21x faster                                                  |
| fannkuch                | 317 ms                                                 | 262 ms: 1.21x faster                                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.37 ms: 1.21x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.9 ms: 1.19x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.2 ms: 1.19x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 63.3 ms: 1.18x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.33 ms: 1.18x faster                                                 |
| gunicorn                | 1.35 ms                                                | 1.15 ms: 1.17x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.17 ms: 1.17x faster                                                 |
| unpack_sequence         | 37.4 ns                                                | 32.0 ns: 1.17x faster                                                 |
| aiohttp                 | 1.27 ms                                                | 1.09 ms: 1.17x faster                                                 |
| coroutines              | 20.2 ms                                                | 17.3 ms: 1.16x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.27 us: 1.16x faster                                                 |
| generators              | 32.7 ms                                                | 28.3 ms: 1.16x faster                                                 |
| scimark_fft             | 230 ms                                                 | 200 ms: 1.15x faster                                                  |
| sympy_expand            | 275 ms                                                 | 241 ms: 1.14x faster                                                  |
| sympy_str               | 169 ms                                                 | 148 ms: 1.14x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 173 ms: 1.14x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 82.6 ms: 1.13x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.43 ms: 1.13x faster                                                 |
| nqueens                 | 68.2 ms                                                | 60.6 ms: 1.13x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 48.2 ms: 1.12x faster                                                 |
| regex_effbot            | 2.46 ms                                                | 2.20 ms: 1.12x faster                                                 |
| pylint                  | 307 ms                                                 | 277 ms: 1.11x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 499 us: 1.10x faster                                                  |
| json_dumps              | 8.40 ms                                                | 7.68 ms: 1.09x faster                                                 |
| json                    | 3.08 ms                                                | 2.82 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.21 ms: 1.08x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 67.3 ms: 1.07x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.55 sec: 1.07x faster                                                |
| telco                   | 3.63 ms                                                | 3.41 ms: 1.06x faster                                                 |
| json_loads              | 16.9 us                                                | 15.9 us: 1.06x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 74.7 ms: 1.05x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 102 ms: 1.05x faster                                                  |
| asyncio_tcp             | 670 ms                                                 | 648 ms: 1.03x faster                                                  |
| pickle                  | 7.35 us                                                | 7.15 us: 1.03x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.6 us: 1.02x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.65 us: 1.01x faster                                                 |
| comprehensions          | 17.6 us                                                | 17.5 us: 1.01x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                 |
| regex_dna               | 162 ms                                                 | 171 ms: 1.06x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 43.2 ms: 1.09x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 9.78 ms: 1.10x slower                                                 |
| regex_v8                | 17.6 ms                                                | 19.8 ms: 1.13x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: coverage
