
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 4fe1c4b
- commit date: 2023-04-15
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 161 ms: 1.25x faster                                   |
| chameleon      | 5.79 ms                                                | 4.23 ms: 1.37x faster                                  |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.22x faster                                 |
| html5lib       | 44.2 ms                                                | 34.9 ms: 1.27x faster                                  |
| tornado_http   | 91.5 ms                                                | 68.5 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 56.7 ms: 1.64x faster                                  |
| float          | 72.4 ms                                                | 50.9 ms: 1.42x faster                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 72.3 ms: 1.33x faster                                  |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.09x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 182 us: 1.56x faster                                   |
| unpickle_pure_python | 203 us                                                 | 137 us: 1.48x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.04 ms: 1.39x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 34.5 ms: 1.30x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 49.0 ms: 1.10x faster                                  |
| unpickle             | 9.89 us                                                | 8.99 us: 1.10x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 97.5 ms: 1.09x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 68.4 ms: 1.06x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| unpickle_list        | 2.69 us                                                | 2.62 us: 1.02x faster                                  |
| pickle               | 7.35 us                                                | 7.50 us: 1.02x slower                                  |
| pickle_dict          | 17.9 us                                                | 18.5 us: 1.03x slower                                  |
| pickle_list          | 2.80 us                                                | 2.91 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 11.5 ms: 1.04x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 9.51 ms: 1.07x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.04 ms: 1.49x faster                                  |
| genshi_xml      | 37.2 ms                                                | 26.4 ms: 1.41x faster                                  |
| genshi_text     | 18.4 ms                                                | 13.4 ms: 1.37x faster                                  |
| django_template | 27.3 ms                                                | 20.2 ms: 1.35x faster                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.50 ms: 2.06x faster                                  |
| logging_silent          | 119 ns                                                 | 62.1 ns: 1.92x faster                                  |
| richards                | 51.4 ms                                                | 30.7 ms: 1.68x faster                                  |
| nbody                   | 93.3 ms                                                | 56.7 ms: 1.64x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 831 us: 1.64x faster                                   |
| scimark_lu              | 109 ms                                                 | 67.3 ms: 1.62x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 992 us: 1.59x faster                                   |
| asyncio_tcp             | 670 ms                                                 | 429 ms: 1.56x faster                                   |
| pickle_pure_python      | 283 us                                                 | 182 us: 1.56x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.10 ms: 1.54x faster                                  |
| scimark_sor             | 126 ms                                                 | 81.8 ms: 1.54x faster                                  |
| raytrace                | 325 ms                                                 | 212 ms: 1.54x faster                                   |
| async_tree_memoization  | 490 ms                                                 | 320 ms: 1.53x faster                                   |
| go                      | 165 ms                                                 | 110 ms: 1.50x faster                                   |
| mako                    | 10.5 ms                                                | 7.04 ms: 1.49x faster                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 48.9 ms: 1.48x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 137 us: 1.48x faster                                   |
| chaos                   | 66.7 ms                                                | 45.2 ms: 1.48x faster                                  |
| crypto_pyaes            | 78.1 ms                                                | 53.4 ms: 1.46x faster                                  |
| generators              | 32.7 ms                                                | 22.5 ms: 1.45x faster                                  |
| async_tree_none         | 400 ms                                                 | 277 ms: 1.44x faster                                   |
| async_tree_io           | 1.02 sec                                               | 716 ms: 1.42x faster                                   |
| float                   | 72.4 ms                                                | 50.9 ms: 1.42x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 24.3 us: 1.42x faster                                  |
| spectral_norm           | 95.8 ms                                                | 67.8 ms: 1.41x faster                                  |
| genshi_xml              | 37.2 ms                                                | 26.4 ms: 1.41x faster                                  |
| pycparser               | 916 ms                                                 | 658 ms: 1.39x faster                                   |
| json_dumps              | 8.40 ms                                                | 6.04 ms: 1.39x faster                                  |
| pyflate                 | 453 ms                                                 | 327 ms: 1.39x faster                                   |
| pprint_safe_repr        | 606 ms                                                 | 440 ms: 1.38x faster                                   |
| genshi_text             | 18.4 ms                                                | 13.4 ms: 1.37x faster                                  |
| chameleon               | 5.79 ms                                                | 4.23 ms: 1.37x faster                                  |
| pprint_pformat          | 1.23 sec                                               | 902 ms: 1.37x faster                                   |
| django_template         | 27.3 ms                                                | 20.2 ms: 1.35x faster                                  |
| logging_simple          | 4.63 us                                                | 3.46 us: 1.34x faster                                  |
| tornado_http            | 91.5 ms                                                | 68.5 ms: 1.34x faster                                  |
| regex_compile           | 96.4 ms                                                | 72.3 ms: 1.33x faster                                  |
| deepcopy                | 281 us                                                 | 211 us: 1.33x faster                                   |
| thrift                  | 580 us                                                 | 440 us: 1.32x faster                                   |
| logging_format          | 4.97 us                                                | 3.79 us: 1.31x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 34.5 ms: 1.30x faster                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.83 us: 1.30x faster                                  |
| scimark_fft             | 230 ms                                                 | 179 ms: 1.29x faster                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.71 ms: 1.28x faster                                  |
| sqlglot_optimize        | 38.0 ms                                                | 29.9 ms: 1.27x faster                                  |
| dulwich_log             | 37.1 ms                                                | 29.2 ms: 1.27x faster                                  |
| unpack_sequence         | 37.4 ns                                                | 29.5 ns: 1.27x faster                                  |
| html5lib                | 44.2 ms                                                | 34.9 ms: 1.27x faster                                  |
| create_gc_cycles        | 880 us                                                 | 700 us: 1.26x faster                                   |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.07 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 533 ms: 1.25x faster                                   |
| 2to3                    | 201 ms                                                 | 161 ms: 1.25x faster                                   |
| fannkuch                | 317 ms                                                 | 257 ms: 1.23x faster                                   |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.22x faster                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 61.6 ms: 1.22x faster                                  |
| mypy2                   | 307 ms                                                 | 256 ms: 1.20x faster                                   |
| pylint                  | 307 ms                                                 | 256 ms: 1.20x faster                                   |
| bench_thread_pool       | 546 us                                                 | 455 us: 1.20x faster                                   |
| sqlglot_normalize       | 196 ms                                                 | 164 ms: 1.20x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.2 ms: 1.18x faster                                  |
| coroutines              | 20.2 ms                                                | 17.2 ms: 1.17x faster                                  |
| sympy_expand            | 275 ms                                                 | 237 ms: 1.16x faster                                   |
| sympy_str               | 169 ms                                                 | 148 ms: 1.14x faster                                   |
| nqueens                 | 68.2 ms                                                | 59.9 ms: 1.14x faster                                  |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                  |
| comprehensions          | 17.6 us                                                | 15.8 us: 1.12x faster                                  |
| json                    | 3.08 ms                                                | 2.78 ms: 1.11x faster                                  |
| mdp                     | 1.66 sec                                               | 1.50 sec: 1.11x faster                                 |
| xml_etree_generate      | 54.2 ms                                                | 49.0 ms: 1.10x faster                                  |
| sympy_sum               | 93.6 ms                                                | 84.9 ms: 1.10x faster                                  |
| unpickle                | 9.89 us                                                | 8.99 us: 1.10x faster                                  |
| meteor_contest          | 78.1 ms                                                | 71.3 ms: 1.09x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.09x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 97.5 ms: 1.09x faster                                  |
| regex_dna               | 162 ms                                                 | 149 ms: 1.09x faster                                   |
| telco                   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                  |
| pathlib                 | 28.8 ms                                                | 27.2 ms: 1.06x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 68.4 ms: 1.06x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| python_startup          | 11.9 ms                                                | 11.5 ms: 1.04x faster                                  |
| unpickle_list           | 2.69 us                                                | 2.62 us: 1.02x faster                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.01x slower                                  |
| pickle                  | 7.35 us                                                | 7.50 us: 1.02x slower                                  |
| pickle_dict             | 17.9 us                                                | 18.5 us: 1.03x slower                                  |
| pickle_list             | 2.80 us                                                | 2.91 us: 1.04x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.61 ms: 1.06x slower                                  |
| python_startup_no_site  | 8.88 ms                                                | 9.51 ms: 1.07x slower                                  |
| async_generators        | 234 ms                                                 | 257 ms: 1.10x slower                                   |
| bench_mp_pool           | 39.7 ms                                                | 45.1 ms: 1.14x slower                                  |
| dask                    | 265 ms                                                 | 314 ms: 1.19x slower                                   |
| coverage                | 42.0 ms                                                | 52.1 ms: 1.24x slower                                  |
| Geometric mean          | (ref)                                                  | 1.26x faster                                           |
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn
