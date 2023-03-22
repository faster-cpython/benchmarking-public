
# Results vs. 3.10.4

- fork: python
- ref: 5b3a2569f4b4dfb58a8f
- machine: darwin-arm64
- commit hash: 5b3a256
- commit date: 2022-09-19
- overall geometric mean: 1.21x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.69 ms: 1.24x faster                                                 |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| html5lib       | 44.2 ms                                                | 35.8 ms: 1.23x faster                                                 |
| tornado_http   | 91.5 ms                                                | 69.4 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.4 ms: 1.43x faster                                                 |
| float          | 72.4 ms                                                | 55.9 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.6 ms: 1.28x faster                                                 |
| regex_v8       | 17.6 ms                                                | 16.7 ms: 1.05x faster                                                 |
| regex_dna      | 162 ms                                                 | 155 ms: 1.04x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.67 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.09 ms: 1.38x faster                                                 |
| pickle_pure_python   | 283 us                                                 | 206 us: 1.37x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 161 us: 1.26x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 47.5 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 64.8 ms: 1.11x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.54 us: 1.06x faster                                                 |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| unpickle             | 9.89 us                                                | 9.68 us: 1.02x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| pickle               | 7.35 us                                                | 7.52 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.22 ms: 1.29x faster                                                 |
| python_startup_no_site | 8.88 ms                                                | 7.30 ms: 1.22x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.14 ms: 1.29x faster                                                 |
| django_template | 27.3 ms                                                | 21.8 ms: 1.25x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 30.1 ms: 1.23x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.3 ms: 1.20x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.83 ms: 1.82x faster                                                 |
| logging_silent          | 119 ns                                                 | 66.5 ns: 1.80x faster                                                 |
| richards                | 51.4 ms                                                | 33.3 ms: 1.54x faster                                                 |
| raytrace                | 325 ms                                                 | 215 ms: 1.52x faster                                                  |
| scimark_lu              | 109 ms                                                 | 72.4 ms: 1.51x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 52.0 ms: 1.50x faster                                                 |
| nbody                   | 93.3 ms                                                | 65.4 ms: 1.43x faster                                                 |
| async_tree_none         | 400 ms                                                 | 282 ms: 1.42x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.6 ms: 1.40x faster                                                 |
| go                      | 165 ms                                                 | 118 ms: 1.40x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 732 ms: 1.39x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.09 ms: 1.38x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 206 us: 1.37x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.00 ms: 1.36x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.17 ms: 1.35x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 54.4 ms: 1.33x faster                                                 |
| tornado_http            | 91.5 ms                                                | 69.4 ms: 1.32x faster                                                 |
| chaos                   | 66.7 ms                                                | 50.7 ms: 1.32x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 72.9 ms: 1.31x faster                                                 |
| thrift                  | 580 us                                                 | 443 us: 1.31x faster                                                  |
| pyflate                 | 453 ms                                                 | 350 ms: 1.29x faster                                                  |
| float                   | 72.4 ms                                                | 55.9 ms: 1.29x faster                                                 |
| python_startup          | 11.9 ms                                                | 9.22 ms: 1.29x faster                                                 |
| mako                    | 10.5 ms                                                | 8.14 ms: 1.29x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 381 ms: 1.29x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.92 ms: 1.28x faster                                                 |
| pycparser               | 916 ms                                                 | 713 ms: 1.28x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| regex_compile           | 96.4 ms                                                | 75.6 ms: 1.28x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 29.1 ms: 1.27x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.65 us: 1.27x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 529 ms: 1.26x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 161 us: 1.26x faster                                                  |
| logging_format          | 4.97 us                                                | 3.94 us: 1.26x faster                                                 |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.07 ms: 1.26x faster                                                 |
| django_template         | 27.3 ms                                                | 21.8 ms: 1.25x faster                                                 |
| scimark_sor             | 126 ms                                                 | 101 ms: 1.24x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.69 ms: 1.24x faster                                                 |
| html5lib                | 44.2 ms                                                | 35.8 ms: 1.23x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 30.1 ms: 1.23x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.24 ms: 1.23x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.83 ms: 1.22x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 61.3 ms: 1.22x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 496 ms: 1.22x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 1.01 sec: 1.22x faster                                                |
| python_startup_no_site  | 8.88 ms                                                | 7.30 ms: 1.22x faster                                                 |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| bench_thread_pool       | 546 us                                                 | 455 us: 1.20x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 28.7 us: 1.20x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.3 ms: 1.20x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.9 ms: 1.19x faster                                                 |
| deepcopy                | 281 us                                                 | 240 us: 1.17x faster                                                  |
| fannkuch                | 317 ms                                                 | 272 ms: 1.17x faster                                                  |
| async_generators        | 234 ms                                                 | 201 ms: 1.16x faster                                                  |
| pylint                  | 307 ms                                                 | 264 ms: 1.16x faster                                                  |
| scimark_fft             | 230 ms                                                 | 199 ms: 1.16x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.07 us: 1.15x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 47.5 ms: 1.14x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.7 ms: 1.14x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 174 ms: 1.12x faster                                                  |
| generators              | 32.7 ms                                                | 29.2 ms: 1.12x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 64.8 ms: 1.11x faster                                                 |
| nqueens                 | 68.2 ms                                                | 61.2 ms: 1.11x faster                                                 |
| sympy_expand            | 275 ms                                                 | 248 ms: 1.11x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| sympy_str               | 169 ms                                                 | 154 ms: 1.10x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 34.2 ns: 1.09x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.53 sec: 1.09x faster                                                |
| json                    | 3.08 ms                                                | 2.84 ms: 1.09x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 86.1 ms: 1.09x faster                                                 |
| 2to3                    | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| telco                   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.54 us: 1.06x faster                                                 |
| regex_v8                | 17.6 ms                                                | 16.7 ms: 1.05x faster                                                 |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| regex_dna               | 162 ms                                                 | 155 ms: 1.04x faster                                                  |
| coroutines              | 20.2 ms                                                | 19.5 ms: 1.04x faster                                                 |
| unpickle                | 9.89 us                                                | 9.68 us: 1.02x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.45 us: 1.02x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 77.9 ms: 1.00x faster                                                 |
| pickle_list             | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| pickle                  | 7.35 us                                                | 7.52 us: 1.02x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 41.4 ms: 1.04x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.67 ms: 1.09x slower                                                 |
| coverage                | 42.0 ms                                                | 53.3 ms: 1.27x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (2): pickle_dict, pidigits
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220919-3.12.0a0-5b3a256/bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256.json: mypy
