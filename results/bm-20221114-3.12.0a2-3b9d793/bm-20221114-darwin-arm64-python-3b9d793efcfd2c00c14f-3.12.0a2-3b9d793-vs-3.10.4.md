
# Results vs. 3.10.4

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: darwin-arm64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 167 ms: 1.21x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.44 ms: 1.30x faster                                                 |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.21x faster                                                |
| html5lib       | 44.2 ms                                                | 35.9 ms: 1.23x faster                                                 |
| tornado_http   | 91.5 ms                                                | 71.3 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.8 ms: 1.42x faster                                                 |
| float          | 72.4 ms                                                | 56.3 ms: 1.29x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.0 ms: 1.27x faster                                                 |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                 |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 205 us: 1.38x faster                                                  |
| json_dumps           | 8.40 ms                                                | 6.12 ms: 1.37x faster                                                 |
| xml_etree_process    | 44.8 ms                                                | 35.5 ms: 1.26x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.26x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.7 ms: 1.11x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 96.3 ms: 1.10x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 69.6 ms: 1.04x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.59 us: 1.04x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle               | 7.35 us                                                | 7.44 us: 1.01x slower                                                 |
| pickle_list          | 2.80 us                                                | 2.85 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.3 ms: 1.04x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 10.2 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.18 ms: 1.46x faster                                                 |
| django_template | 27.3 ms                                                | 21.4 ms: 1.27x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 29.6 ms: 1.26x faster                                                 |
| genshi_text     | 18.4 ms                                                | 14.8 ms: 1.24x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.68 ms: 1.92x faster                                                 |
| logging_silent          | 119 ns                                                 | 67.1 ns: 1.78x faster                                                 |
| richards                | 51.4 ms                                                | 32.0 ms: 1.61x faster                                                 |
| scimark_lu              | 109 ms                                                 | 70.0 ms: 1.56x faster                                                 |
| raytrace                | 325 ms                                                 | 214 ms: 1.52x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 51.9 ms: 1.50x faster                                                 |
| mako                    | 10.5 ms                                                | 7.18 ms: 1.46x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 338 ms: 1.45x faster                                                  |
| nbody                   | 93.3 ms                                                | 65.8 ms: 1.42x faster                                                 |
| go                      | 165 ms                                                 | 119 ms: 1.39x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 205 us: 1.38x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.12 ms: 1.37x faster                                                 |
| async_tree_none         | 400 ms                                                 | 294 ms: 1.36x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.01 ms: 1.36x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 755 ms: 1.35x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.17 ms: 1.34x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 54.6 ms: 1.33x faster                                                 |
| pycparser               | 916 ms                                                 | 696 ms: 1.32x faster                                                  |
| thrift                  | 580 us                                                 | 442 us: 1.31x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 73.0 ms: 1.31x faster                                                 |
| chaos                   | 66.7 ms                                                | 51.0 ms: 1.31x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.44 ms: 1.30x faster                                                 |
| pyflate                 | 453 ms                                                 | 351 ms: 1.29x faster                                                  |
| float                   | 72.4 ms                                                | 56.3 ms: 1.29x faster                                                 |
| tornado_http            | 91.5 ms                                                | 71.3 ms: 1.28x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.63 us: 1.28x faster                                                 |
| django_template         | 27.3 ms                                                | 21.4 ms: 1.27x faster                                                 |
| create_gc_cycles        | 880 us                                                 | 693 us: 1.27x faster                                                  |
| regex_compile           | 96.4 ms                                                | 76.0 ms: 1.27x faster                                                 |
| logging_format          | 4.97 us                                                | 3.92 us: 1.27x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 35.5 ms: 1.26x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 162 us: 1.26x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 29.6 ms: 1.26x faster                                                 |
| hexiom                  | 6.32 ms                                                | 5.04 ms: 1.25x faster                                                 |
| genshi_text             | 18.4 ms                                                | 14.8 ms: 1.24x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.79 ms: 1.24x faster                                                 |
| html5lib                | 44.2 ms                                                | 35.9 ms: 1.23x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 30.2 ms: 1.23x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 1.01 sec: 1.22x faster                                                |
| pprint_safe_repr        | 606 ms                                                 | 497 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 555 ms: 1.21x faster                                                  |
| 2to3                    | 201 ms                                                 | 167 ms: 1.21x faster                                                  |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.21x faster                                                |
| scimark_sor             | 126 ms                                                 | 105 ms: 1.20x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 31.8 ms: 1.19x faster                                                 |
| fannkuch                | 317 ms                                                 | 271 ms: 1.17x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 29.5 us: 1.17x faster                                                 |
| scimark_fft             | 230 ms                                                 | 198 ms: 1.16x faster                                                  |
| mypy2                   | 307 ms                                                 | 264 ms: 1.16x faster                                                  |
| dask                    | 265 ms                                                 | 229 ms: 1.16x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 473 us: 1.16x faster                                                  |
| deepcopy                | 281 us                                                 | 243 us: 1.15x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.07 us: 1.15x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.7 ms: 1.13x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 174 ms: 1.12x faster                                                  |
| async_generators        | 234 ms                                                 | 208 ms: 1.12x faster                                                  |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 48.7 ms: 1.11x faster                                                 |
| sympy_expand            | 275 ms                                                 | 248 ms: 1.11x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 96.3 ms: 1.10x faster                                                 |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                                 |
| sympy_str               | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| telco                   | 3.63 ms                                                | 3.35 ms: 1.08x faster                                                 |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.55 sec: 1.07x faster                                                |
| pathlib                 | 28.8 ms                                                | 26.9 ms: 1.07x faster                                                 |
| nqueens                 | 68.2 ms                                                | 63.9 ms: 1.07x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 87.7 ms: 1.07x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.40 us: 1.06x faster                                                 |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 69.6 ms: 1.04x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.59 us: 1.04x faster                                                 |
| asyncio_tcp             | 670 ms                                                 | 650 ms: 1.03x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 76.7 ms: 1.02x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                 |
| pickle                  | 7.35 us                                                | 7.44 us: 1.01x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.85 us: 1.01x slower                                                 |
| coroutines              | 20.2 ms                                                | 20.6 ms: 1.02x slower                                                 |
| comprehensions          | 17.6 us                                                | 18.0 us: 1.02x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.3 ms: 1.04x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                 |
| generators              | 32.7 ms                                                | 35.8 ms: 1.09x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 44.5 ms: 1.12x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 10.2 ms: 1.14x slower                                                 |
| coverage                | 42.0 ms                                                | 60.5 ms: 1.44x slower                                                 |
| unpack_sequence         | 37.4 ns                                                | 62.8 ns: 1.68x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
